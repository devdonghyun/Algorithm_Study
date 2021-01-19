def distanceFromOrigin(coor):
    coor.sort(key=lambda c: abs(0-c[0]) + abs(0-c[1]))
    for val in coor:
        print(val[2])


n = int(input())
coor = []
for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    coor.append((x, y, i+1))
distanceFromOrigin(coor)
