from fastapi import FastAPI
#from cnetmobile import main, CnetMobile
from cnetmobile_update import main, CnetMobile

app = FastAPI()    

@app.get("/cnetmobile")
async def trigger(compra_numero: str, qtdItens: int):
    dados = CnetMobile()
    lista_itens = list(range(1, qtdItens+1))
    await main(dados, lista_itens, compra_numero)
    #await main(dados, compra_numero)
    dados.translate()
    
    # response = {
    #     'compra': dados.compra,
    #     'itens': dados.itens,
    #     'propostas': dados.propostas
    # }
    
    response = {
        'propostas': dados.propostas
    }

    import json
    with open('examples/latest/propostas.json', 'w', encoding='utf-8') as json_file:
        json.dump(dados.propostas, json_file, indent=2, ensure_ascii=False)
        
    # with open('examples/latest/itens.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(dados.itens, json_file, indent=2, ensure_ascii=False)
        
    # with open('examples/latest/compra.json', 'w', encoding='utf-8') as json_file:
    #     json.dump(dados.compra, json_file, indent=2, ensure_ascii=False)

    return response