from fastapi import FastAPI
from cnetmobile import main, CnetMobile

app = FastAPI()    

@app.get("/cnetmobile")
async def trigger(compra_numero: str):
    dados = CnetMobile()
    await main(dados, compra_numero)
    dados.translate()
    
    response = {
        'compra': dados.compra,
        'itens': dados.itens,
        'propostas': dados.propostas
    }
    
    import json
    with open('examples/latest/propostas.json', 'w', encoding='utf-8') as json_file:
        json.dump(dados.propostas, json_file, indent=2, ensure_ascii=False)
        
    with open('examples/latest/itens.json', 'w', encoding='utf-8') as json_file:
        json.dump(dados.itens, json_file, indent=2, ensure_ascii=False)
        
    with open('examples/latest/compra.json', 'w', encoding='utf-8') as json_file:
        json.dump(dados.compra, json_file, indent=2, ensure_ascii=False)

    return response