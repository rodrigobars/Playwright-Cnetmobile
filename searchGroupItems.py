import aiohttp
import asyncio

async def fetch_data(session, url, group):
    async with session.get(url) as response:
        json_response = await response.json()
        if json_response:
            return {group: json_response}
        return
    
async def searchGroupItems(compra_numero):
    group = -1
    total_groups = 20  # Primeira rodada de 10 requisições
    groupItensList = []
    groupItensDicio = {}

    async with aiohttp.ClientSession() as session:
        while True:
            tasks = []
            for _ in range(total_groups):
                url = f'https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-fase-externa/public/v1/compras/{compra_numero}/itens/{group}/itens-grupo?tamanhoPagina=10000&pagina=0'
                print('Requisitando -> ', url)
                tasks.append(fetch_data(session, url, group))
                group -= 1

            results = await asyncio.gather(*tasks)

            non_empty_results = [dicio for dicio in results if dicio]
            [groupItensDicio.update(item) for item in non_empty_results]

            if non_empty_results:
                groupItensList.extend(non_empty_results)

                # Verifica se todos os resultados são não vazios
                if len(non_empty_results) == len(results):
                    total_groups = 10  # Adiciona mais 10 requisições
                else:
                    break  # Se houver algum retorno vazio, interrompe o loop
            else:
                break  # Se todos os resultados forem vazios, interrompe o loop

    return groupItensDicio