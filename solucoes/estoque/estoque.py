import sys

tiptam = list(map(int, sys.stdin.readline().split()))

estoque = []
for _ in range(tiptam[0]):
    estoque.append(list(map(int, sys.stdin.readline().split())))

vendas = int(sys.stdin.readline())
efetivas = 0

for _ in range(vendas):
    pedido = list(map(int, sys.stdin.readline().split())) # tipo, tamanho
    if estoque[pedido[0]-1][pedido[1]-1] > 0:
        estoque[pedido[0]-1][pedido[1]-1] -= 1
        efetivas += 1

sys.stdout.write(str(efetivas))