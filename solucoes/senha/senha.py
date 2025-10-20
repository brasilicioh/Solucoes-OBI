caracteristicaSenha = list(map(int, input().split())) # num caracteres senha, num letras borradas, length cada palavra
senha = input()

palavras = [sorted(input()) for _ in range(caracteristicaSenha[1])]

indiceSenha = int(input())

indiceBorradas = []
for i in range(caracteristicaSenha[0]):
    if senha[i] == "#":
        indiceBorradas.append(i)

