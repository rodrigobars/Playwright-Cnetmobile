import asyncio
from playwright.async_api import async_playwright
from urllib.parse import urlparse, parse_qs, urlencode
from dataclasses import dataclass, field
from typing import Dict, List, Any
from Enum_classes.Enum import Enum
from Enum_classes.Itens import Itens
from Enum_classes.Propostas import Propostas
from Enum_classes.Compra import Compra
from pprint import pprint

@dataclass
class CnetMobile:
    compra: Dict[str, Any] = field(default_factory=dict)
    enum: Dict[str, Any] = field(default_factory=dict)
    itens: List[Dict[str, Any]] = field(default_factory=list)
    propostas: List[Dict[str, Any]] = field(default_factory=list)
    compra_collected: bool = False
    enum_collected: bool = False
    
    def translate(self):
        # Utilizando Enuns para decodificar os json's
        Enum.feed(self.enum)
        self.compra = Compra(**self.compra).to_dict()
        self.itens = Itens(self.itens).to_list()
        self.propostas = Propostas(self.propostas).to_list()

async def on_message(msg):
    if msg['type'] == 'elementFound':
        pass

async def on_block(msg, page, url):
    if msg['type'] == 'blocked':
        print("blocked...")
        await page.goto(url)

async def custom_route_handler(route, json_captured, page, dados, status, paginaCnetmobile):
    url = route.request.url
    parsed_url = urlparse(url)
    last_path = parsed_url.path.split('/')[-1]
    second_last_path = parsed_url.path.split('/')[-2]
    
    if '/comprasnet-fase-externa/public/v1/' in parsed_url.path:
        
        # Obtém os parâmetros da consulta
        query_parameters = parse_qs(parsed_url.query)

        # Modifica os parâmetros conforme necessário
        if 'tamanhoPagina' in query_parameters.keys():
            query_parameters['tamanhoPagina'] = ['20']
            query_parameters['pagina'] = [paginaCnetmobile]

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
            
        if 'itens' == last_path:
            if json_data:
                status.qtdItens = len(json_data)
                dados.itens += json_data

                json_captured.set()
            else:
                status.qtdItens = 0
                json_captured.set()
            print('qtf itens: ',len(json_data))
            
        elif 'propostas' == last_path:
            if 'itens-grupo' == second_last_path:
                
                status.companys_captured += 1

                for item in json_data:
                    if item['numero'] not in status.item_propostas:
                        proposta = item.pop('propostaItem')
                        status.item_propostas.update({item['numero']: [proposta]})
                        status.item_conteudo.update({item['numero']: item})
                    else:
                        status.item_propostas[item['numero']].append(item['propostaItem'])

                if status.companys_captured == status.companys_to_capture:
                    print(f"\nQuantidade de propostas do grupo concluída")
                    for key, value in status.item_conteudo.items():
                        value.update({'propostasItem': status.item_propostas[key]})

                    for proposta in dados.propostas:
                        if proposta['numero'] == status.actual_item:
                            proposta['subItens'] += [item for item in status.item_conteudo.values()]

                    json_captured.set()

            elif json_data['tipo'] == 'G':
                status.actual_item = json_data['numero']
                status.qtdeItensDoGrupo = json_data['qtdeItensDoGrupo']
                json_data.update( {'subItens': []} )
                dados.propostas.append(json_data)

                if len(json_data['propostasItem']) > 15:
                    status.companys_to_capture = 15
                else:
                    status.companys_to_capture = len(json_data['propostasItem'])

                print(f"Grupo: {json_data['identificador']} | Participantes: {status.companys_to_capture}")

                if status.companys_to_capture > 0:
                    await page.evaluate('getGrupoPropostas();')
                else:
                    json_captured.set()

            else:
                dados.propostas.append(json_data)
                json_captured.set()
            
        else:
            if not dados.compra_collected:
                dados.compra = json_data
                dados.compra_collected = True
                
    elif '/comprasnet-fase-externa/v1/enums' in parsed_url.path:
        response = await route.fetch(url=url)
        json_data = await response.json()
        if not dados.enum_collected:
            dados.enum = json_data
            dados.enum_collected = True
        await route.fulfill(response=response, json=json_data)
        
    else:
        await route.continue_()

async def fazer_requisicao(dados, browser, url, semaforo, paginaCnetmobile=0):
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

        status = Status()

        context = await browser.new_context(viewport={"width": 800, "height": 500})
        await context.add_init_script(path='preload.js')
        await context.add_init_script(path='groupGetter.js')
        page = await context.new_page()

        # Expor a função para o contexto da página
        await page.expose_function('postMessage', on_message)
        
        # Defina a função para ser executada quando a página recarregar
        await page.expose_function('ping_block', lambda msg: on_block(msg, page, url))
        
        await page.route("**/*", lambda route: custom_route_handler(route, json_captured, page, dados, status, paginaCnetmobile))
        await page.goto(url)
        print(f'Iniciando a requisição: {url}')

        await json_captured.wait()

        await page.close()
        await context.close()
    return status.qtdItens
        
def mount_urls(url_base, compra_numero, lista_itens):
    urls = []
    for itemPropostas in lista_itens:
        urls.append(f"{url_base}/item/{itemPropostas['numero']}?compra={compra_numero}")
    print(f"URLS A SEREM REQUISITADOS: {urls}")
    return(urls)

async def main(dados, compra_numero):
    # Número máximo de requisições simultâneas
    limite_simultaneo = 4
    semaforo = asyncio.Semaphore(limite_simultaneo)
    
    #compra_numero = linkSistemaOrigem.split("compra=")[1]
    url_base = "https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-web/public/compras/acompanhamento-compra"
    url_itens = f'{url_base}?compra={compra_numero}'
    
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)

        n = 3
        itensPageCnetmobile = list(range(n))
        while itensPageCnetmobile:
            tasks = []
            for itemPage in itensPageCnetmobile:
                task = asyncio.ensure_future(fazer_requisicao(dados, browser, url_itens, semaforo, paginaCnetmobile=itemPage))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
            print(f'Resultados da requisição: {results}')

            if sum(results) < 60:
                break
            else:
                itensPageCnetmobile = [n + x for x in itensPageCnetmobile]

        print(dados.itens, '\n')
        
        for item in dados.itens:
            print('Item: ', item['numero'])
        
        urls = mount_urls(url_base=url_base, compra_numero=compra_numero, lista_itens=dados.itens)

        # Lista para armazenar tarefas de requisição
        tasks = []
        
        # Criar tarefas para cada requisição
        for url in urls:
            print(f'Adicionando task => {url}')
            task = asyncio.ensure_future(fazer_requisicao(dados, browser, url, semaforo))
            tasks.append(task)

        await asyncio.gather(*tasks)