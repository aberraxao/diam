function calcularPotencia() {
    let b = parseInt(document.getElementById("base").value);
    let e = parseInt(document.getElementById("expoente").value);
    let res = b ** e;
    document.getElementById("resultado").textContent = "O resultado é: " + res;
}

function trocaLink() {
    document.getElementById("link1").innerText = "ISCTE";
    document.getElementById("link1").href = "https://www.iscte-iul.pt/";
    document.getElementById("btn1").remove();
}