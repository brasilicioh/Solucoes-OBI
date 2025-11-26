# Feito por Kaio Henrique

n = int(input())
I = []
maxsize = 0
R = set()
L = 0

for i in range(n):
    I.append(int(input()))

for elmnt in range(len(I)):
    while I[elmnt] in R:
        R.remove(I[L])
        L += 1
    else:
        R.add(I[elmnt])
        size = elmnt - L + 1
        maxsize = max(maxsize, size)
    
print(max(maxsize, size))

# Código testado e aprovado com corretor automático usando: https://github.com/brasilicioh/Solucoes-OBI/
# Max runtime: 0.050s