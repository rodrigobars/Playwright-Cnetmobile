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
            delay += 4000
        }
    }, 100);

}

async function getItemsDetails() {

    setTimeout(async () => {
        const companys = document.getElementsByClassName("ng-trigger-animationRotate180");
        const filteredElements = Array.from(companys);
      
        // Track the number of pending clicks
        let pendingClicks = filteredElements.length;
      
        // Function to handle individual clicks with a delay
        const handleClickWithDelay = async (item, delay) => {
            await new Promise(resolve => setTimeout(resolve, delay)); // Wait for the delay
            item.click();
            pendingClicks--;
      
            // Check if all clicks have finished
            if (pendingClicks === 0) {
                let filteredElements3
                let delay = 1000
                const companys2 = document.getElementsByClassName("ng-trigger-animationRotate180");
                const filteredElements2 = Array.from(companys2);
    
                // Criar um conjunto de elementos únicos a partir de filteredElements2
                const uniqueElements2 = new Set(filteredElements2);
                
                // Filtrar filteredElements2 removendo elementos já presentes em filteredElements
                filteredElements2.forEach((element2) => {
                    if (filteredElements.includes(element2)) {
                    uniqueElements2.delete(element2);
                    }
                });
    
                // Converter o conjunto uniqueElements2 em um array
                filteredElements3 = Array.from(uniqueElements2);
                    
                filteredElements3.forEach((element) => {
                    setTimeout(() => {
                        element.click()
                    }, delay)
                    delay += 1000
                }, delay)
            }
        };
      
        // Initiate clicks with delays
        for (const [index, item] of filteredElements.entries()) {
            await handleClickWithDelay(item, 1000); // Use index-based delay
        }
    })

}

//}

// const getItemsDetails = async () => {
//     setTimeout(() => {
//         const companys = document.getElementsByClassName("ng-trigger-animationRotate180");
//         const filteredElements = Array.from(companys);

//         let clickedItemsCount = 0;
//         let filteredElements3
//         let delay = 1000;

//         filteredElements.forEach((item) => {
//             setTimeout(() => {
//                 item.click();
//                 clickedItemsCount += 1
//             }, delay);
//             delay += 1000;
//         });

//         setTimeout(() => {
//             const companys2 = document.getElementsByClassName("ng-trigger-animationRotate180");
//             const filteredElements2 = Array.from(companys2);
    
//             // Criar um conjunto de elementos únicos a partir de filteredElements2
//             const uniqueElements2 = new Set(filteredElements2);
            
//             // Filtrar filteredElements2 removendo elementos já presentes em filteredElements
//             filteredElements2.forEach((element2) => {
//                 if (filteredElements.includes(element2)) {
//                 uniqueElements2.delete(element2);
//                 }
//             });
    
//             // Converter o conjunto uniqueElements2 em um array
//             filteredElements3 = Array.from(uniqueElements2);
                
//             filteredElements3.forEach((element) => {
//                 setTimeout(() => {
//                     element.click()
//                 }, delay)
//                 delay += 1000
//             }, delay)

//         }, delay)

//         // filteredElements3 agora contém apenas os elementos novos que não estão em filteredElements
//     }, 1000)
// }


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