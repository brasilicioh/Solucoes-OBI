from sys import stdin as inp, stdout as out

qtdAtletas = int(inp.readline())

atletaPosicao = {}

for i in range(qtdAtletas):
    atleta = int(inp.readline())
    atletaPosicao[atleta] = i+1

for i in sorted(atletaPosicao.items()):
    print(i[1])