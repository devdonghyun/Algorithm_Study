
from collections import deque

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input())))


def inRange(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


def bfs(x, y):
    d_x = [-1, 1, 0, 0]
    d_y = [0, 0, -1, 1]
    count = 1
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x, new_y = x + d_x[i], y + d_y[i]
            if inRange(new_x, new_y) and grid[new_x][new_y] == 1:
                grid[new_x][new_y] = grid[x][y] + 1
                queue.append((new_x, new_y))


bfs(0, 0)
print(grid[n-1][m-1])
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()
