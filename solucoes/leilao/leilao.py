# pessoa = ""
# valor = 0
# qtd = int(input())
# for _ in range(qtd):
#     nome = input().strip()
#     num = int(input())
#     if num > valor:
#         valor = num
#         pessoa = nome
# print(pessoa)
# print(valor)

from sys import stdin as inp
lances = {}
qtd = int(inp.readline())
for _ in range(qtd):
    nome = inp.readline().strip()
    valor = int(inp.readline())
    if nome in lances.keys():
        if valor > lances[nome]:
            lances[nome] = valor
    else:
        lances[nome] = valor
ordenado = dict(sorted(lances.items(), key=lambda lance: lance[1], reverse=True))
print(list(ordenado.keys())[0])
print(list(ordenado.values())[0])


