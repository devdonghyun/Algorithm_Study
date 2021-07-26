from collections import deque

n, l, r = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

d_x = [-1, 1, 0, 0]
d_y = [0, 0, -1, 1]


def inRange(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    popu_list.append(grid[x][y])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_x, new_y = x + d_x[i], y + d_y[i]

            if inRange(new_x, new_y) and visited[new_x][new_y] == 0 and l <= abs(grid[new_x][new_y] - grid[x][y]) <= r:
                popu_list.append(grid[new_x][new_y])
                visited[new_x][new_y] = 1
                queue.append((new_x, new_y))


count = 0
while True:
    visited = [[0] * n for _ in range(n)]
    popu_list = []
    for i in range(n):
        for j in range(n):
            bfs(i, j)
    if len(popu_list) == 1:
        break
    count += 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                grid[i][j] = sum(popu_list) // len(popu_list)

    print(grid)
    print(popu_list)
    break

print(count)
