$(document).ready(function () {
    let imagem_perfil_xs = $("#imagem_perfil_xs");
    let picture_username = $("#picture_username");
    let botao_questoes = $("#botao_questoes");
    let lista_questoes = $("#lista_questoes");
    let imagem_perfil_xl = $("#imagem_perfil_xl");
    let detalhes_perfil = $("#detalhes_perfil");

    imagem_perfil_xs.dblclick(function () {
        imagem_perfil_xs.hide();
    })

    picture_username.click(function () {
        imagem_perfil_xs.show();
    })

    botao_questoes.click(function () {
        lista_questoes.toggle();
        botao_questoes.text(lista_questoes.is(":visible") ? "Esconder questões" : "Mostrar questões");
    });

    imagem_perfil_xl.mouseenter(function () {
        detalhes_perfil.show();
        detalhes_perfil
            .animate({width: "40%"}, 500)
            .animate({fontSize: "20px"}, 1000)
    });

    imagem_perfil_xl.mouseleave(function () {
        detalhes_perfil
            .animate({width: "30%"}, 500)
            .animate({fontSize: "14px"}, 1000)
            .promise()
            .done(function () {
                $(this).fadeOut(500);
            });
    });
})
