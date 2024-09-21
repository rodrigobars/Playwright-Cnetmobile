from playwright.async_api import async_playwright
import subprocess
import asyncio

async def start_chrome_with_debugging(executable_path, port):
    command = f'"{executable_path}" --remote-debugging-port={port} --no-sandbox'
    print(command)
    #command = 'chrome-stable --remote-debugging-port={port} --no-sandbox'
    process = subprocess.Popen(command, shell=True)
    return process, port

def stop_chrome(process):
    process.terminate()

async def custom_route_handler(route):
    print(route.request.url)
    response = await route.fetch(url=route.request.url)

    content_type = response.headers.get("content-type", "")
    
    if "application/json" in content_type:
        try:
            json_data = await response.json()
            print(json_data)

        except Exception as e:
            print(f"Erro ao ler JSON da resposta: {e}")

        await route.fulfill(response=response, json=json_data)

    else:
        await route.continue_()

async def main():
    async with async_playwright() as p:
        # with open('preload.js', 'r') as file:
        #     js = file.read()

        try:
            chrome_process, port = await start_chrome_with_debugging(
                executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe',
                port=9222
            )

            while True:
                try:
                    browser = await p.chromium.connect_over_cdp(
                        endpoint_url=f"http://localhost:{port}",
                        slow_mo=200
                    )
                    print('Conectado')
                    break
                except:
                    await asyncio.sleep(0.1)

            default_context = browser.contexts[0]
            page = default_context.pages[0]

            # Adiciona o script preload.js na página
            #await page.add_init_script(js)

            # Navega para a página
            await page.route("**/*", lambda route: custom_route_handler(route))
            await page.goto("https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-web/public/compras/acompanhamento-compra/item/1?compra=15018205900282024")
            await page.wait_for_load_state(state='networkidle')

            # Executa a função
            #await page.evaluate("initial_page()")

            await page.close()
            stop_chrome(chrome_process)
        except Exception as e:
            print(f'{str(e)}')
            await page.close()
            stop_chrome(chrome_process)

# Executa o código assíncrono
asyncio.run(main())
