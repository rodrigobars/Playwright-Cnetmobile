from playwright.async_api import async_playwright
import asyncio

async def custom_route_handler(route):
    print(route.request.url)
    response = await route.fetch(url=route.request.url)

    content_type = response.headers.get("content-type", "")
    
    if "application/json" in content_type:
        try:
            json_data = await response.json()
            print(json_data)

            if "hcaptchaHabilitado" in list(json_data.keys()):
                json_data["hcaptchaHabilitado"] = False

        except Exception as e:
            print(f"Erro ao ler JSON da resposta: {e}")

        await route.fulfill(response=response, json=json_data)

    else:
        await route.continue_()

async def main():

    user_profile_path = "/home/rodrigo/snap/firefox/common/.mozilla/firefox/p5wko2fq.default-1724696942566"

    async with async_playwright() as p:

        # Definindo as preferências para restaurar as abas anteriores
        firefox_args = [
            "--restore-last-session"  # Esse argumento tenta restaurar a última sessão
        ]

        # Inicializando o Firefox com as preferências configuradas e o perfil de usuário
        browser_context = await p.firefox.launch_persistent_context(
            user_profile_path, 
            headless=False, 
            firefox_user_prefs={
                "browser.startup.page": 5,  # 3: Restaurar abas e janelas anteriores
            },
            args=firefox_args
        )

        # Exibindo títulos das abas já abertas
        for page in browser_context.pages:
            print(f"Abas abertas: {await page.title()}")

        # Abrindo uma nova aba
        # new_page = await browser_context.new_page()
        # await new_page.route("**/*", lambda route: custom_route_handler(route))
        # await asyncio.sleep(1)
        # await new_page.goto('https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-web/public/compras/acompanhamento-compra?compra=15018205900282024')
        # await asyncio.sleep(50)

asyncio.run(main())