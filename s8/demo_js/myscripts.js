function fatorial(n) {
    let f = 1;
    for (let i = 1; i <= n; i++) {
        f = f * i;
    }
    return f;
}

function calcularFatorial() {
    let num = prompt("Introduza um numero inteiro positivo: ");
// parseInt() converte de string para numero inteiro
    let f = fatorial(parseInt(num));
    document.write('O fatorial de ' + num + ' é: ' + f);
}