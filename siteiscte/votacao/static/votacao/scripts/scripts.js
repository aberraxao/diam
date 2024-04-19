$(document).ready(function () {
    let botao_questoes = $("#botao_questoes");
    let lista_questoes = $("#lista_questoes")

    botao_questoes.click(function () {
        lista_questoes.toggle();
        if (lista_questoes.is(":visible")) {
            botao_questoes.text("Esconder Questões");
        } else {
            botao_questoes.text("Mostrar Questões");
        }
    });
})