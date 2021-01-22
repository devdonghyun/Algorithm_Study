from collections import deque


def inRange(x, y):
    return 0 <= x < n and 0 <= y < m


def canGo(x, y):
    if not inRange(x, y):
        return False
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    return True


def BFS():
    global escape
    d_x, d_y = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            new_x = x + d_x[i]
            new_y = y + d_y[i]
            if canGo(new_x, new_y):
                if new_x == n-1 and new_y == m-1:
                    escape = 1
                    return
                q.append((new_x, new_y))
                visited[new_x][new_y] = 1


n, m = input().split()
n, m = int(n), int(m)
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]
q = deque()
escape = 0
q.append((0, 0))
BFS()
print(escape)
