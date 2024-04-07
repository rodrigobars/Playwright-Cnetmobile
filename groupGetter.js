const getGrupoPropostas = async () => {
 
    setTimeout(() => {
        const companys = document.getElementsByClassName("ng-trigger-animationRotate180");
        const filteredElements = Array.from(companys).filter((element, index) => index > 0);
        filteredElements.forEach((item) => item.click())

        const buttonsProposta = Array.from(document.querySelectorAll('button'))
            .filter(el => el.textContent === 'Proposta');
        
        let delay = 1000;

        // Loop para clicar nos botões com delay individual
        for (const button of buttonsProposta) {
            setTimeout(() => {
                button.click();
            }, delay);
            delay += 1500
        }
    }, 100);

}