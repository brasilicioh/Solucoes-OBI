def anagrama(palavra1: str, palavra2: str) -> bool:
    return sorted(palavra1) == sorted(palavra2)

def raiz_poligrama(tamanho: int, palavra: str) -> str:
    for tamRaiz in range(1, tamanho//2):
        if tamanho % tamRaiz == 0:
            raiz = palavra[:tamRaiz]
            partesDaPalavra = [palavra[i:(i+tamRaiz)] for i in range(0, tamanho, tamRaiz)]

            if all(anagrama(raiz, parte) for parte in partesDaPalavra):
                return raiz

    return "*"

numCarac = int(input())
palavra = input()

print(raiz_poligrama(numCarac, palavra))