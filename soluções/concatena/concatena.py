from sys import stdin as inp, stdout as out

def calulaPotencial(lista: list) -> int:
    if len(lista) == 1:
        return 0
    potencial = 0
    for index, num in enumerate(lista):
        soma = 0
        for index2, otoNum in enumerate(lista):
            if index == index2:
                continue
            soma += int("".join([num, otoNum]))
        potencial += soma
    return potencial



numLista, numPerguntas = map(int, inp.readline().split())
lista = inp.readline().split()
potenciais = []
for _ in range(numPerguntas):
    pos1, pos2 = map(int, inp.readline().split())
    pos1 -= 1
    listAnalisada = lista[pos1:pos2]
    potenciais.append(calulaPotencial(listAnalisada))

for potencial in potenciais:
    out.write(str(potencial) + "\n")

#!/usr/bin/env python3

# [n, q] = [int(x) for x in input().split()]
# v = [int(x) for x in input().split()]

# psum = []
# soma = 0
# for x in v:
#   soma += x
#   psum.append(soma)

# respostas = []
# while q > 0:
#   [l, r] = [int(x) for x in input().split()]
#   l -= 1
#   r -= 1
#   tam = r - l + 1
#   if l == 0:
#     soma = psum[r]
#   else:
#     soma = psum[r] - psum[l - 1]
#   resp = (tam - 1) * soma * 11
#   respostas.append(resp)
#   q -= 1

# for i in respostas:
#   print(i)