S = int(input())
n1 = int(input())
n2 = int(input())

nums = 0

soma = 0

for i in range(n1, n2+1):
    for j in str(i):
        soma += int(j)
    if soma == S:
        nums += 1
    soma = 0

print(nums)