def inRange(x, y):
    return 0 <= x < n and 0 <= y < m


def canGo(x, y):
    if not inRange(x, y):
        return False
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    return True


def canEscape(x, y):
    global escape
    d_x = [1, 0]
    d_y = [0, 1]

    for i in range(2):
        new_x = x + d_x[i]
        new_y = y + d_y[i]

        if canGo(new_x, new_y):
            if new_x == n-1 and new_y == m-1:
                escape = 1
                return
            visited[new_x][new_y] = 1
            canEscape(new_x, new_y)


n, m = input().split()
n, m = int(n), int(m)
escape = 0
grid = []
visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
canEscape(0, 0)
print(escape)
