from sys import stdin as inp, stdout as out

lins, cols, ordens = map(int, inp.readline().split())

linArray = list(range(lins))
colArray = list(range(cols))

comandos = []
for _ in range(ordens):
    comando = inp.readline().strip().split()
    if len(comandos) > 0 and (comandos[-1] == comando or (comandos[-1][1] == comando[2] and comandos[-1][2] == comando[1])):
        comandos.pop()
        continue
    comandos.append(comando)

for ordem in comandos:
    if ordem[0] == "L":
        linArray[int(ordem[1])-1], linArray[int(ordem[2])-1] = linArray[int(ordem[2])-1], linArray[int(ordem[1])-1]
    elif ordem[0] == "C":
        colArray[int(ordem[1])-1], colArray[int(ordem[2])-1] = colArray[int(ordem[2])-1], colArray[int(ordem[1])-1]
    dancaFeita = [ordem[0], ordem[1], ordem[2]]

for i in range(lins):
    for j in range(cols):
        out.write(str(1 + (linArray[i]*cols+colArray[j])))
        out.write(" " if j != cols-1 else "")
    out.write("\n")