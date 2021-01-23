def inRange(x, y):
    return 0 <= x < n and 0 <= y < n


def canPop(new_x, new_y):
    if not inRange(new_x, new_y):
        return False
    if visited[new_x][new_y] == 1:
        return False
    return True


def PuyoPuyo(x, y):
    global count
    d_x, d_y = [0, 1, 0, -1], [1, 0, -1, 0]

    for i in range(4):
        new_x = x + d_x[i]
        new_y = y + d_y[i]

        if canPop(new_x, new_y):
            if grid[new_x][new_y] != grid[x][y]:
                continue
            count += 1
            visited[new_x][new_y] = 1
            PuyoPuyo(new_x, new_y)


n = int(input())
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]
popList = []
count = 0
for i in range(n):
    for j in range(n):
        if canPop(i, j):
            count = 1
            visited[i][j] = 1
            PuyoPuyo(i, j)
            popList.append(count)

pop_count = 0
for val in popList:
    if val >= 4:
        pop_count += 1

print(pop_count, max(popList))


# print([citizenList[i] for i in range(len(citizenList)) if citizenList[i] != 0])
