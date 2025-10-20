from sys import stdin as inp, stdout as out

numArara, numGaiola = map(int, inp.readline().split())

espacosArara = numArara*5-4

print("S" if espacosArara <= numGaiola else "N")