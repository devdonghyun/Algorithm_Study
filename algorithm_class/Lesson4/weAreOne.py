from collections import deque


def inRange(x, y):
    return 0 <= x < n and 0 <= y < n


def canGo(x, y):
    if not inRange(x, y):
        return False
    if visited[x][y] == 1:
        return False
    return True


def weAreOne():
    count_all = []
    d_x, d_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            new_x = x + d_x[i]
            new_y = y + d_y[i]
            if canGo(new_x, new_y):
                if u > abs(grid[new_x][new_y] - grid[x][y]) or d < abs(grid[new_x][new_y] - grid[x][y]):
                    continue
                q.append((new_x, new_y))
                visited[new_x][new_y] = 1
                count += 1
        count_all.append(count)
    return count_all


n, k, u, d = input().split()
n, k, u, d = int(n), int(k), int(u), int(d)
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]
q = deque()
q.append((0, 0))
count_all = weAreOne()
print(max(count_all))
print(count_all)
