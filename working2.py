import pychrome
import time
import subprocess
from urllib.parse import urlparse
import json
import os
import asyncio

def start_chrome_with_debugging(executable_path, port):
    command = f'"{executable_path}" --remote-debugging-port={port}'
    process = subprocess.Popen(command, shell=True)
    return process, port

def stop_chrome(process):
    process.terminate()

def monitorar_trafego(browser, url, propostas):
    # tab0 = browser.list_tab()[0]
    # tab = browser.new_tab()
    # browser.close_tab(tab_id=tab0.id)
    # browser.activate_tab(tab_id=tab.id)

    tab = browser.new_tab()

    def request_will_be_sent(**kwargs):
        pass
        #print("Requisição:", kwargs)
        # if 'request' in kwargs and 'postData' in kwargs['request']:
        #     print("\nDados da requisição:", kwargs['request']['postData'])

    def response_received(**kwargs):
        #print("Resposta:", kwargs)
        if 'response' in kwargs:
            request_id = kwargs['requestId']
            parsed_url = urlparse(kwargs['response']['url'])
            last_path = parsed_url.path.split('/')[-1]
            if last_path == 'propostas':
                try:
                    body_response = tab.call_method("Network.getResponseBody", requestId=request_id)
                    body = body_response.get('body')

                    #print("Raw response body:", body)  # Inspect the raw response

                    if not body:
                        print("Response body is empty.")
                        return  # Early exit if empty

                    # Attempt to load the JSON
                    json_data = json.loads(body)

                    propostas.append(json_data)

                finally:
                    browser.close_tab(tab_id=tab.id)

    tab.start()
    tab.call_method("Network.setUserAgentOverride", userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/92.0")
    tab.call_method("Network.enable")
    tab.set_listener("Network.requestWillBeSent", request_will_be_sent)
    tab.set_listener("Network.responseReceived", response_received)

    tab.call_method("Page.navigate", url=url)

    time.sleep(4)

    tab.stop()

if __name__ == "__main__":
    pregao = '900372024'
    
    chrome_process, port = start_chrome_with_debugging(
            executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe',
            port=9222
        )
    
    browser = pychrome.Browser(url=f"http://127.0.0.1:{port}")
    
    propostas = []

    for item in range(1, 98):
        url = f"https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-web/public/compras/acompanhamento-compra/item/{item}?compra=15018205{pregao}"
        monitorar_trafego(browser, url, propostas)

        try:
            # Ensure the directory exists
            directory = f'dados/{pregao}'
            os.makedirs(directory, exist_ok=True)

            # Save the parsed JSON data to a file
            with open(f'{directory}/propostas.json', 'w', encoding='utf-8') as json_file:
                json.dump(propostas, json_file, indent=2, ensure_ascii=False)
                print('Data saved successfully!')

        except json.JSONDecodeError as e:
            print(f'JSON decode error: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')

    print('FINALIZADO!')
    stop_chrome(chrome_process)
