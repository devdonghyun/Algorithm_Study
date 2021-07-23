n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input())))


def inRange(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


def dfs(x, y):
    if not inRange(x, y):
        return False

    if grid[x][y] == 0:
        grid[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)
