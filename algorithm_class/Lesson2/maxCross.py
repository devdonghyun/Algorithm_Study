import copy


def inRange(x, y):
    return 0 <= x < n and 0 <= y < n


def maxCross(n, grid, i, j):
    tmp = copy.deepcopy(grid)
    bound = grid[i][j]
    tmp[i][j] = 0
    for k in range(4):
        x, y = i, j
        for _ in range(bound):
            if k == 0:
                x -= 1
            elif k == 1:
                x += 1
            elif k == 2:
                y -= 1
            else:
                y += 1
            if not inRange(x, y):
                break
            tmp[x][y] = 0
    tmp2 = copy.deepcopy(tmp)

    for i in range(n):
        tmp_row = n-1
        for j in range(n-1, -1, -1):
            if tmp[j][i] != 0:
                tmp2[tmp_row][i] = tmp[j][i]
                tmp_row -= 1
    print(tmp2)
    count = 0
    for row in range(n):
        for col in range(n):
            if col+1 >= n:
                continue
            for i in range(n):
                for j in range(col, col+2):
                    if j+1 >= n:
                        continue
                    if tmp2[i][j] == tmp2[i][j+1]:
                        if tmp2[i][j] == 0:
                            continue
                        count += 1

    for row in range(n):
        for col in range(n):
            if row+1 >= n:
                continue
            for i in range(n):
                for j in range(row, row+2):
                    if j+1 >= n:
                        continue
                    if tmp2[j][i] == tmp2[j+1][i]:
                        if tmp2[j][i] == 0:
                            continue
                        count += 1
    return count


n = int(input())
grid = []
max_count = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
for i in range(n):
    for j in range(n):
        count = maxCross(n, grid, i, j)
        max_count.append(count)
print(max_count)
print(max(max_count))
