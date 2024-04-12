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
            delay += 3000
        }
    }, 100);

}



//elementos por índice:
// buttonNodes[0] - Botão principal de expansão
// buttonNodes[1] - Chat
// buttonNodes[2] - Proposta
// buttonNodes[buttonNodes.length - 1]; - Anexos

// const dataViewContent = document.getElementsByClassName('p-dataview-content');
// const dataViewContentListNodes = dataViewContent[0].childNodes;
// const divNodes = Array.prototype.filter.call(dataViewContentListNodes, function(node) {
//     return node.nodeType === Node.ELEMENT_NODE && node.tagName === 'DIV';
// });

// for (const companyNode of divNodes) {
    
//     setTimeout(() => {
//         const buttonNodes = companyNode.getElementsByTagName('BUTTON');
        
//         buttonNodes[0].click();
//         buttonNodes[2].click();

//         let delay = 1000;

//         const qtdItens = buttonNodes.length - 4
    
//         for (let i = 3; i < (2*qtdItens)+3; i+=2) {
//             setTimeout(() => {
//                 buttonNodes[i].click();
//             }, delay);
//             delay += 3000
//         }
//     }, 400)
// }