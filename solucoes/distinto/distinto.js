var n, num;
scanf("%d", "n");

var numeros = [];
for (var i = 0; i < n; i++) {
    scanf("%d", "num");
    numeros.push(num);
}

var intervalo = new Set();
var inicioInterval = 0, maxInterval = 0;
for (var fimInterval = 0; fimInterval < n; fimInterval++) {
    while (intervalo.has(numeros[fimInterval])) {
        intervalo.delete(numeros[inicioInterval]);
        inicioInterval++;
    }
    intervalo.add(numeros[fimInterval]);
    maxInterval = Math.max(maxInterval, fimInterval - inicioInterval + 1);
}

printf("%d\n", maxInterval);