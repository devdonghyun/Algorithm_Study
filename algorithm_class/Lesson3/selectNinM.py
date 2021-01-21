def selectMinN():
    if cnt == n:
        return
    for i in range(n-1):
        for j in range(m):
            dist += (coor[i+1][j] - coor[i][j])**2


n, m = input().split()
n, m = int(n), int(m)
coor = []
for i in range(n):
    f, s = input().split()
    f, s = int(f), int(s)
    coor.append([f, s])
