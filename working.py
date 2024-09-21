import pychrome
import time

def monitorar_trafego(url):
    browser = pychrome.Browser(url="http://127.0.0.1:9222")
    tab = browser.new_tab()

    def request_will_be_sent(**kwargs):
        print("Requisição:", kwargs)
        if 'request' in kwargs and 'postData' in kwargs['request']:
            print("\nDados da requisição:", kwargs['request']['postData'])

    def response_received(**kwargs):
        print("Resposta:", kwargs)
        if 'response' in kwargs:
            request_id = kwargs['requestId']
            # Recupera o corpo da resposta
            try:
                body = tab.call_method("Network.getResponseBody", requestId=request_id)
                print("\nCorpo da Resposta:", body.get('body'))
            except:
                print('sem dados.')

    tab.start()
    tab.call_method("Network.enable")
    tab.set_listener("Network.requestWillBeSent", request_will_be_sent)
    tab.set_listener("Network.responseReceived", response_received)

    tab.call_method("Page.navigate", url=url)

    time.sleep(10)  # Ajuste conforme necessário

    tab.stop()

if __name__ == "__main__":
    url_alvo = "https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-web/public/compras/acompanhamento-compra/item/1?compra=15018205900332024"
    monitorar_trafego(url_alvo)
