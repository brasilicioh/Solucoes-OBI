# Exemplo de uso do repositório: soma de dois inteiros
# teste com: "python validar.py _exemplo.py" no terminal

import sys

inp = sys.stdin.readline
out = sys.stdout.write

n1 = int(inp())
n2 = int(inp())

out(str(n1+n2))