from collections import deque


def inRange(x, y):
    return 0 <= x < n and 0 <= y < n


def canGo(x, y):
    if not inRange(x, y):
        return False
    if visited[x][y] == 1:
        return False
    return True


def rottenTangerine():

    d_x, d_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    time = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            new_x = x + d_x[i]
            new_y = y + d_y[i]
            if canGo(new_x, new_y):
                if grid[new_x][new_y] == 0 or grid[new_x][new_y] == -1:
                    a[new_x][new_y] = -1
                    continue
                if grid[new_x][new_y] == 2:
                    continue

                time += 1
                q.append((new_x, new_y))
                if a[new_x][new_y] >= time:
                    a[new_x][new_y] = time
                visited[new_x][new_y] = 1


n, k = input().split()
n, k = int(n), int(k)
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]
a = [
    [0 for _ in range(n)]
    for _ in range(n)
]
q = deque()
rottenList = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            rottenList.append((i, j))

for i in range(len(rottenList)):
    x, y = rottenList[i]
    a[x][y] = 0
    q.append(x, y)
    rottenTangerine()
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
