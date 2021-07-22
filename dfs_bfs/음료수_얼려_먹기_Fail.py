from collections import deque


def inRange(x, y):
    if 0 <= x <= n-1 and 0 <= y <= m-1:
        return True
    else:
        return False


def bfs(grid, visited):
    count = 0
    for x in range(n):
        for y in range(m):
            queue = deque([(x, y)])
            visited[x][y] = 1
            while queue:
                x, y = queue.popleft()
                if grid[x][y] == 0 and visited[x][y] == 0:
                    visited[x][y] = 1
                    for i in range(4):
                        new_x, new_y = x + d_x[i], y + d_y[i]
                        if inRange(new_x, new_y) and grid[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
                            queue.append((new_x, new_y))
                        else:
                            count += 1

    print(count)


n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = []
    line = input()
    for i in range(m):
        row.append(int(line[i]))
    grid.append(row)

d_x = [-1, 1, 0, 0]
d_y = [0, 0, -1, 1]

visited = [[0] * m for _ in range(n)]

bfs(grid, visited)
