$(document).ready(function () {
    const palavras_insultuosas = [
        'abécula', 'abentesma', 'achavascado', 'alimária', 'andrajoso',
        'barregã', 'biltre', 'cacóstomo', 'cuarra', 'estólido',
        'estroso', 'estultilóquio', 'nefelibata', 'néscio', 'pechenga',
        'sevandija', 'somítico', 'tatibitate', 'xexé', 'cheché',
        'xexelento'
    ];

    let imagem_perfil_xs = $("#imagem-perfil-xs");
    let username = $("#username");
    let botao_questoes = $("#botao-questoes");
    let lista_questoes = $("#lista-questoes");
    let imagem_perfil_xl = $("#imagem-perfil-xl");
    let detalhes_perfil = $("#detalhes-perfil");

    imagem_perfil_xs.dblclick(function () {
        imagem_perfil_xs.hide();
    })

    username.click(function () {
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


    $('#comentario').on('input', function () {
        let comentario = $(this).val().toLowerCase();
        let contem_insultos = false;

        $.each(palavras_insultuosas, function (index, palavra) {
            if (comentario.indexOf(palavra) !== -1) {
                contem_insultos = true;
                return false;
            }
        });

        if (contem_insultos) {
            $('#comentario').val('');
            $('#comentario-feedback-ko').show();
            $('#comentario-feedback-ok').hide();
        } else {
            $('#comentario-feedback-ko').hide();
            $('#comentario-feedback-ok').show();
        }
    });
});
