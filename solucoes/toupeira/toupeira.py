import sys

saloes, tuneis = map(int, sys.stdin.readline().split())

allPossibles = set()
for _ in range(tuneis):
    inicio, fim = map(int, sys.stdin.readline().split())
    allPossibles.add((inicio, fim))
    allPossibles.add((fim, inicio))

numSugestoes = int(sys.stdin.readline())
sugestoesValidas = 0
for _ in range(numSugestoes):
    sugestaoPasseio = sys.stdin.readline().strip().split()
    numSaloes = sugestaoPasseio[0]
    sugestaoPasseio.remove(numSaloes)

    passeioPossivel = True
    for i in range(int(numSaloes)-1):
        inicioPasseio = int(sugestaoPasseio[i])
        fimPasseio = int(sugestaoPasseio[i+1])
        if (inicioPasseio, fimPasseio) not in allPossibles:
            passeioPossivel = False
            break

    if passeioPossivel:
        sugestoesValidas += 1

sys.stdout.write(str(sugestoesValidas))