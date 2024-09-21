import asyncio
from playwright.async_api import async_playwright
from urllib.parse import urlparse, parse_qs, urlencode
from dataclasses import dataclass, field
from typing import Dict, List, Any
from Enum_classes.Enum import Enum
from Enum_classes.Propostas import Propostas
from Enum_classes.Compra import Compra
from searchGroupItems import searchGroupItems

@dataclass
class CnetMobile:
    enum: Dict[str, Any] = field(default_factory=dict)
    propostas: List[Dict[str, Any]] = field(default_factory=list)
    enum_collected: bool = False
    
    def translate(self):
        # Utilizando Enuns para decodificar os json's
        Enum.feed(self.enum)
        self.propostas = Propostas(self.propostas).to_list()

async def on_message(msg):
    if msg['type'] == 'elementFound':
        pass

async def on_block(msg, page, url):
    if msg['type'] == 'blocked':
        print("blocked...")
        await asyncio.sleep(5)
        await page.goto(url)

async def custom_route_handler(route, json_captured, dados, status, groupItems, groupID):
    url = route.request.url
    parsed_url = urlparse(url)
    last_path = parsed_url.path.split('/')[-1]
    
    if '/comprasnet-fase-externa/public/v1/' in parsed_url.path:
        
        # Obtém os parâmetros da consulta
        query_parameters = parse_qs(parsed_url.query)

        # Modifica os parâmetros conforme necessário
        if 'tamanhoPagina' in query_parameters.keys():
            query_parameters['tamanhoPagina'] = ['20']
            query_parameters['pagina'] = ['0']

            # Atualiza a URL com os parâmetros modificados
            url = parsed_url._replace(query=urlencode(query_parameters, doseq=True)).geturl()
        
        response = await route.fetch(url=url)

        content_type = response.headers.get("content-type", "")
        
        if "application/json" in content_type:
            try:
                json_data = await response.json()
                #print(f'JSON => {json_data}')
            except Exception as e:
                print(f"Erro ao ler JSON da resposta: {e}")
        else:
            json_data = {}
            
        await route.fulfill(response=response, json=json_data)
            
        if 'propostas' == last_path:
            try:
                if 'status' in list(json_data.keys()): 
                    print('revogado')
                    if json_data['status'] == '422': # "Campo item não pode ser nulo"
                        json_captured.set()
                if json_data['tipo'] == 'S': # S = Subitem
                    for key, value in groupItems.items():
                        for item in value:
                            if json_data['numero'] == item['numero']:
                                json_data['grupo'] = groupID[key]

                dados.propostas.append(json_data)
                json_captured.set()
            except:
                json_captured.set()
                
    elif '/comprasnet-fase-externa/v1/enums' in parsed_url.path:
        response = await route.fetch(url=url)
        json_data = await response.json()
        if not dados.enum_collected:
            dados.enum = json_data
            dados.enum_collected = True
        await route.fulfill(response=response, json=json_data)
        
    else:
        await route.continue_()

async def fazer_requisicao(dados, context, url, semaforo, groupItems=None, groupID=None):
    async with semaforo:
        json_captured = asyncio.Event()

        @dataclass
        class Status:
            companys_to_capture = None
            companys_captured = 0
            actual_item = None
            isFirstJsonGroup = True
            broughtData = False
            data = None
            qtdItens = 0
            qtdeItensDoGrupo = 0
            item_propostas = {}
            item_conteudo = {}
            dicionario_de_itens = None

        status = Status()

        page = await context.new_page()
        await page.add_init_script(path='preload.js')

        # Expor a função para o contexto da página
        await page.expose_function('postMessage', on_message)
        
        # Defina a função para ser executada quando a página recarregar
        await page.expose_function('ping_block', lambda msg: on_block(msg, page, url))
        
        await page.route("**/*", lambda route: custom_route_handler(route, json_captured, dados, status, groupItems, groupID))
        await page.goto(url)
        print(f'Iniciando a requisição: {url}')

        await json_captured.wait()

        await page.close()
    return status.qtdItens
        
def mount_urls(url_base, compra_numero, lista_itens):
    urls = []
    for item in lista_itens:
        urls.append(f"{url_base}/item/{item}?compra={compra_numero}")
    print(f"URLS A SEREM REQUISITADOS: {urls}")
    return(urls)

async def main(dados, lista_itens: list, compra_numero):
    # Número máximo de requisições simultâneas
    #limite_simultaneo_inicial = 1
    limite_simultaneo_inicial = 1
    limite_simultaneo_aumentado = 1
    semaforo = asyncio.Semaphore(limite_simultaneo_inicial)
    
    #compra_numero = linkSistemaOrigem.split("compra=")[1]
    url_base = "https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-web/public/compras/acompanhamento-compra"

    groupItems = await searchGroupItems(compra_numero=compra_numero)
    groupID = None

    if groupItems:
        groupKeyList = list(groupItems.keys())
        lista_itens.extend(groupKeyList)

        groupID = {}
        for idx, value in enumerate(sorted(groupKeyList), start=1):
            groupID.update({value: f'G{idx}'})

    urls = mount_urls(url_base=url_base, lista_itens=lista_itens, compra_numero=compra_numero)

    async with async_playwright() as p:
        browser = await p.firefox.launch(
            headless=False,
            args=[
                "--autoplay-policy=user-gesture-required",
                "--disable-background-networking",
                "--disable-background-timer-throttling",
                "--disable-backgrounding-occluded-windows",
                "--disable-breakpad",
                "--disable-client-side-phishing-detection",
                "--disable-component-update",
                "--disable-default-apps",
                "--disable-dev-shm-usage",
                "--disable-domain-reliability",
                "--disable-extensions",
                "--disable-features=AudioServiceOutOfProcess",
                "--disable-hang-monitor",
                "--disable-ipc-flooding-protection",
                "--disable-notifications",
                "--disable-offer-store-unmasked-wallet-cards",
                "--disable-popup-blocking",
                "--disable-print-preview",
                "--disable-prompt-on-repost",
                "--disable-renderer-backgrounding",
                "--disable-setuid-sandbox",
                "--disable-speech-api",
                "--disable-sync",
                "--disk-cache-size=33554432",
                "--hide-scrollbars",
                "--ignore-gpu-blacklist",
                "--metrics-recording-only",
                "--mute-audio",
                "--no-default-browser-check",
                "--no-first-run",
                "--no-pings",
                "--no-sandbox",
                "--no-zygote",
                "--password-store=basic",
                "--use-gl=swiftshader",
                "--use-mock-keychain",
                "--single-process",
                "--disable-gpu",
                "--font-render-hinting=none"
            ]
        )

        context = await browser.new_context(viewport={"width": 1600, "height": 800})

        #await context.set_extra_http_headers({'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})

        # Criar tarefas para cada requisição
        tasks = []
        primeira_tarefa = True
        
        for url in urls:
            print(f'Adicionando task => {url}')
            task = asyncio.ensure_future(fazer_requisicao(dados, context, url, semaforo, groupItems, groupID))
            tasks.append(task)

            # if primeira_tarefa:
            #     await task  # Aguarda a conclusão da primeira tarefa
            #     # Aumenta o semáforo para permitir mais requisições simultâneas
            #     semaforo = asyncio.Semaphore(limite_simultaneo_aumentado)
            #     primeira_tarefa = False

        await asyncio.gather(*tasks)

# dados = CnetMobile()
# lista_itens = list(range(1, 147)) # 1-146
# compra_numero = '15018205900362024'

# asyncio.run(main(dados=dados, lista_itens=lista_itens, compra_numero=compra_numero))

# print(dados.propostas)