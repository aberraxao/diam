$(document).ready(function () {
    $("#btn1").click(function () {
        $(".texto1").hide();
        $("#btn1").text("Agora já não funciona...");
    });
});
$(document).ready(function () {
    $("#btnG").click(function () {
        $("p").addClass("green-arial-text");
    });
});
$(document).ready(function () {
    $("#btnN").click(function () {
        $("p").removeClass("green-arial-text");
    });
});