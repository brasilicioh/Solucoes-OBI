# from sys import stdin as inp, stdout as out

# def verificarMessage(alfa: list, text: str) -> str:
#     for i in text:
#         if i not in alfa:
#             return "N"
#     return "S"

# qtdAli, qtdMessage = map(int, inp.readline().split())
# alfabetoAli = sorted(inp.readline().strip())
# message = inp.readline().strip()

# out.write(verificarMessage(alfabetoAli, message))

from sys import stdin as inp, stdout as out

lenAlfa, lenMessage = map(int, inp.readline().split())
alfabeto = inp.readline().strip()
message = inp.readline().strip()
for caractere in message:
    if caractere not in alfabeto:
        out.write("N")
        exit()
out.write("S")