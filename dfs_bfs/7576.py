# 백준 bfs - 7576번: 토마토 <1시간 7분>
# 내가 생각했던 풀이와 좀 많이 달라졌다
# 일수를 체크하려면 최단경로로 탈출하는 문제와 유사하게 해야했다
# 변화가 있을 때와 없을 때의 경우도 다시 알아봐야겠다

from collections import deque

m, n = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

d_x = [-1, 1, 0, 0]
d_y = [0, 0, -1, 1]


def inRange(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs():
    while queue:
        count += 1
        x, y = queue.popleft()
        for i in range(4):
            new_x, new_y = x + d_x[i], y + d_y[i]
            if inRange(new_x, new_y) and grid[new_x][new_y] == 0:
                grid[new_x][new_y] = grid[x][y] + 1
                queue.append((new_x, new_y))


queue = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            queue.append((i, j))

bfs()

day = 1
result = -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            day = 0
        result = max(result, grid[i][j])


if day == 0:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result-1)
