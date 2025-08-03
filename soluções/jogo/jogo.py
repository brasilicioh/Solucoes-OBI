def novaMatriz(matrix: list) -> list:
    newMatriz = [list(i) for i in matrix]
    for lin in range(len(matrix)):
        for col in range(len(matrix)):
            vizinViv = 0

            for vizx in range(-1, 2):
                for vizy in range(-1, 2):
                    if vizx == 0 and vizy == 0: continue
                    posx = lin + vizx
                    posy = col + vizy
                    if 0 <= posx < len(matrix) and 0 <= posy < len(matrix):
                        vizinViv += int(matrix[posx][posy])
            
            if matrix[lin][col] == "1" and vizinViv not in [2, 3]:
                newMatriz[lin][col] = "0"
            elif matrix[lin][col] == "0" and vizinViv == 3:
                newMatriz[lin][col] = "1"

    return newMatriz

ordem_steps = list(map(int, input().split()))
matriz = [input() for i in range(ordem_steps[0])]
for step in range(ordem_steps[1]):
    matriz = novaMatriz(matriz)
for i in range(len(matriz)):
    for j in matriz[i]:
        print(j, end="")
    print()