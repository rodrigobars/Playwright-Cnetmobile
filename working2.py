import pychrome
import time
import subprocess

def start_chrome_with_debugging(executable_path, port):
    command = f'"{executable_path}" --remote-debugging-port={port}'
    process = subprocess.Popen(command, shell=True)
    return process, port

def stop_chrome(process):
    process.terminate()

def monitorar_trafego(url, chrome_process, port):
    browser = pychrome.Browser(url=f"http://127.0.0.1:{port}")
    tab = browser.new_tab()

    def request_will_be_sent(**kwargs):
        print("Requisição:", kwargs)
        if 'request' in kwargs and 'postData' in kwargs['request']:
            print("\nDados da requisição:", kwargs['request']['postData'])

    def response_received(**kwargs):
        print("Resposta:", kwargs)
        if 'response' in kwargs:
            request_id = kwargs['requestId']
            try:
                body = tab.call_method("Network.getResponseBody", requestId=request_id)
                print("\nCorpo da Resposta:", body.get('body'))
            except:
                print('sem dados.')

    tab.start()
    tab.call_method("Network.setUserAgentOverride", userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/92.0")
    tab.call_method("Network.enable")
    tab.set_listener("Network.requestWillBeSent", request_will_be_sent)
    tab.set_listener("Network.responseReceived", response_received)

    tab.call_method("Page.navigate", url=url)

    time.sleep(10)

    tab.stop()
    stop_chrome(chrome_process)

if __name__ == "__main__":
    url_alvo = "https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-web/public/compras/acompanhamento-compra/item/1?compra=15018205900332024"
    
    chrome_process, port = start_chrome_with_debugging(
            executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe',
            port=9222
        )
    
    monitorar_trafego(url_alvo, chrome_process, port)
