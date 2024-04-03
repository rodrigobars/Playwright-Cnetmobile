// preload.js
document.addEventListener('DOMContentLoaded', () => {
    const observeChanges = () => {
        return new Promise((resolve, reject) => {
            const config = {
                subtree: true,
                attributes: true,
                childList: true
            };

            const callback = (mutationList) => {
                // window.postMessage({ type: 'elementFound', data: 'Analisando mudança!\n' });
                for (const mutation of mutationList) {
                    mutation.addedNodes.forEach((addedNode) => {
                        // window.postMessage({ type: 'elementFound', data: 'Analisando nó filho....:' });
                        // window.postMessage({ type: 'elementFound', data: addedNode.tagName });
                        // window.postMessage({ type: 'elementFound', data: addedNode.attributes });
                        // window.postMessage({ type: 'elementFound', data: addedNode.textContent });
                        if (
                            addedNode.tagName == 'P-TOASTITEM' ||
                            addedNode.textContent == 'Não foi possível realizar a validação do Captcha para retornar os dados. Tente mais tarde.'
                        ) {
                            window.ping_block({ type: 'blocked', data: 'BLOCKED!' });
                            // resolve();
                        }
                    });
                }
                reject();
            };

            const observer = new MutationObserver(callback);

            observer.observe(document.body, config);
        });
    };

    const startObserving = async () => {
        try {
            // window.postMessage({ type: 'elementFound', data: '\nIniciando o observer!!!\n' });
            await observeChanges();
            // window.postMessage({ type: 'elementFound', data: 'Elemento encontrado!' });
        } catch (error) {
            // window.postMessage({ type: 'elementFound', data: `----------------- ERRO => ${error} -----------------` });
        }
    };

    // Chama a função startObserving() quando o evento DOMContentLoaded ocorrer
    startObserving();
});

const getGrupoPropostas = async () => {
    const companys = document.getElementsByClassName("ng-trigger-animationRotate180");
    const filteredElements = Array.from(companys).filter((element, index) => index > 0);
    filteredElements.forEach((item) => item.click())

    const buttonsProposta = Array.from(document.querySelectorAll('button'))
        .filter(el => el.textContent === 'Proposta');

    let delay = 0;

    // Loop para clicar nos botões com delay individual
    for (const button of buttonsProposta) {
        setTimeout(() => {
            button.click();
        }, delay);

        delay += 500; // Aumenta o delay para o próximo botão
    }
}