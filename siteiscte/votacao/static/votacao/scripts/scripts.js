$(document).ready(function () {
    let imagem_perfil = $("#imagem_perfil");
    let picture_username = $("#picture_username");
    let botao_questoes = $("#botao_questoes");
    let lista_questoes = $("#lista_questoes");

    imagem_perfil.dblclick(function () {
        imagem_perfil.hide();
    })

    picture_username.click(function () {
        imagem_perfil.show();
    })

    botao_questoes.click(function () {
        lista_questoes.toggle();
        botao_questoes.text(lista_questoes.is(":visible") ? "Esconder questões" : "Mostrar questões");
    });
})