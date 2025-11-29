# Exemplo de uso do repositório: concatenação de n textos
# teste com: "python validar.py _exemplo2.py" no terminal

import sys

inp = sys.stdin.readline
out = sys.stdout.write

n = int(inp())
texts = [inp().strip() for _ in range(n)]

out("".join(texts))