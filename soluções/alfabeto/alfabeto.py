from sys import stdin as inp, stdout as out

def verificarMessage(alfa: list, text: str) -> str:
    for i in text:
        if i not in alfa:
            return "N"
    return "S"

qtdAli, qtdMessage = map(int, inp.readline().split())
alfabetoAli = sorted(inp.readline().strip())
message = inp.readline().strip()

out.write(verificarMessage(alfabetoAli, message))