from sys import stdin as inp, stdout as out

golsP = list(map(int, inp.readline().split()))[1:]
golsC = list(map(int, inp.readline().split()))[1:]

golPau, golCam = 0, 0

out.write(f"{golPau} {golCam}\n")

for _ in range(len(golsP) + len(golsC)):
    minutoP = golsP[golPau] if golPau < len(golsP) else float("inf")
    minutoC = golsC[golCam] if golCam < len(golsC) else float("inf")

    if minutoP < minutoC:
        golPau += 1
        out.write(f"{golPau} {golCam}\n")
    else:
        golCam += 1
        out.write(f"{golPau} {golCam}\n")
