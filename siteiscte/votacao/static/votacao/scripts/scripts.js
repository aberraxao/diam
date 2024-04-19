$(document).ready(function () {
    let botao_questoes = $("#botao_questoes");
    let lista_questoes = $("#lista_questoes")

    botao_questoes.click(function () {
        lista_questoes.toggle();
        botao_questoes.text(lista_questoes.is(":visible") ? "Esconder Questões": "Mostrar Questões");
    });
})