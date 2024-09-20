window.initial_page = function() {

    setTimeout(() => {
        // Situação
        const situacao = document.querySelectorAll("input[type='radio']");
        emAndamento = situacao[0];
        finalizados = situacao[1];
        finalizados.click();
        // finalizados.checked = true;
    }, 1000)

    setTimeout(() => {
        // Situação => Etapa
        if (finalizados.checked) {
            const resultado = document.querySelectorAll('input[type="checkbox"]')
            const desertas = resultado[0]
            const homologadas = resultado[1]
            const preferenciaisMeEpp = resultado[2]
            homologadas.click()
        }else{
            const etapa = document.querySelectorAll(".ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default")
            abertasParaParticipacao = etapa[0]
            emDisputa = etapa[1]
            emSelecaoDeFornecedores = etapa[2]
            abertasParaParticipacao.click() // Desativando (Vem ativo por padrão)
            emSelecaoDeFornecedores.click() // Ativando
        }

        // Modalidade
        const modalidade = document.querySelector('[aria-label="Todas as modalidades"]')
        modalidade.click()
        const pregao = document.querySelector('[aria-label="Pregão"]')
        pregao.click()

        // Criterio de Julgamento
        const criterioDeJulgamento = document.querySelector('[aria-label="Todos os critérios de julgamento"]');
        criterioDeJulgamento.click()
        const menorPrecoMaiorDesconto = document.querySelector('[aria-label="Menor Preço / Maior Desconto"]');
        menorPrecoMaiorDesconto.click()
        
        // ---- Parte de input textual ----
        const unidadeCompradoraENumeroDaCompra = document.querySelectorAll('.ui-inputtext.ui-corner-all.ui-state-default.ui-widget')

        // Unidade Compradora (UASG)
        unidadeCompradora = unidadeCompradoraENumeroDaCompra[0]
        unidadeCompradora.value = '150182'

        numeroDaCompra = unidadeCompradoraENumeroDaCompra[1]
        numeroDaCompra.value = '582023'
        
        a = document.querySelectorAll(".cp-input-valor.ui-inputwrapper-focus.ng-untouched.ng-pristine.ng-valid")
        b = document.querySelectorAll(".ui-inputtext.ui-corner-all.ui-state-default.ui-widget")
        // é preciso clicar aqui

    }, 3000) 

    setTimeout(() => {
        ////////////////////////////////////////
        a[0].classList.remove("ng-untouched", "ng-pristine")
        a[0].classList.add("ui-inputwrapper-filled", "ng-dirty", "ng-touched")
        b[0].classList.add("ui-state-filled")
        b[0].value = '150182'
        b[0].focus()

        a[1].classList.remove("ng-untouched", "ng-pristine")
        a[1].classList.add("ui-inputwrapper-filled", "ng-dirty", "ng-touched")
        b[1].classList.add("ui-state-filled")
        b[1].value = '582023'

        b[1].focus()
        b[0].focus()
        b[1].focus()
        b[0].focus()
    }, 4000)

    setTimeout(() => {
        const buttonElement = document.querySelector('.is-primary[type="button"]')
        buttonElement.click();
    }, 6000)

    setTimeout(() => {
        const a = document.querySelector(".br-button.ml-auto")
        a.click()
        const actionButtons = document.querySelectorAll('.br-button.ml-auto')
        actionButtons[1].click()
    }, 9000)

    setTimeout(() => {
        const download_button = document.querySelector(".ng-star-inserted.ui-menuitem.ui-corner-all.ui-menu-parent")
        download_button.classList.add('ui-menuitem-active')
        const julgamentoHabilitacao = document.querySelector('[title="Download do relatório de julgamento/habilitação"]')
        julgamentoHabilitacao.click()
    }, 13000)
}