import pychrome

# Inicia o navegador com a URL desejada
def monitorar_trafego(url):
    # Conecta ao Chrome
    browser = pychrome.Browser(url="http://127.0.0.1:9222")
    # Cria uma nova aba
    tab = browser.new_tab()

    # Define as funções de callback para monitorar o tráfego
    def request_will_be_sent(**kwargs):
        print("Requisição:", kwargs)

    def response_received(**kwargs):
        print("Resposta:", kwargs)

    # Habilita o rastreamento de rede
    tab.start()
    tab.call_method("Network.enable")

    # Define os callbacks para os eventos de rede
    tab.set_listener("Network.requestWillBeSent", request_will_be_sent)
    tab.set_listener("Network.responseReceived", response_received)

    # Navega para a URL desejada
    tab.call_method("Page.navigate", url=url)
    #tab.call_method("Page.loadEventFired")

    # Aguarda um tempo para capturar o tráfego
    import time
    time.sleep(10)  # Ajuste o tempo conforme necessário

    # Finaliza a aba
    tab.stop()

if __name__ == "__main__":
    url_alvo = "https://cnetmobile.estaleiro.serpro.gov.br/comprasnet-web/public/compras/acompanhamento-compra?compra=15018205900332024"  # Substitua pela URL desejada
    monitorar_trafego(url_alvo)
