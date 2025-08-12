hora, min, seg = (int(input()) for _ in range(3))
newSeg = seg + int(input())
newMin = min
newHour = hora
while newSeg >= 60:
    newMin = (newSeg//60)+min
    newSeg %= 60

while newMin >= 60:
    newHour = (newMin//60)+hora
    newMin %= 60

while newHour >= 24:
    newHour -= 24

print(newHour)
print(newMin)
print(newSeg)