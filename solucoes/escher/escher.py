from sys import stdin as inp, stdout as out

numAlturas = int(inp.readline())
alturas = list(map(int, inp.readline().strip().split()))

for i, (altura1, altura2) in enumerate(zip(alturas, reversed(alturas))):
    if i == 0: 
        soma = altura1 + altura2
    elif i == numAlturas//2 and numAlturas % 2 == 1:
        if altura1 != soma/2 or altura2 != soma/2:
            out.write("N")
            exit()
    else:
        if altura1 + altura2 != soma:
            out.write("N")
            exit()
out.write("S")