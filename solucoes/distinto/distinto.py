from sys import stdin as inp, stdout as out

n = int(inp.readline())

I = [int(inp.readline()) for _ in range(n)]

maxInterval = 0
start = 0
interval = set()

for i in range(n):
    while I[i] in interval:
        interval.remove(I[start])
        start += 1
    interval.add(I[i])
    maxInterval = max(maxInterval, i - start + 1)

out.write(str(maxInterval) + "\n")