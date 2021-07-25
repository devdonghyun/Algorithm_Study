# 백준 dfs - 10026번: 적록색약  <22분 16초>
# 정상인의 시점으로 봤을 때의 수를 세면서 녹색으로 보이는 것을 모두 적색으로 바꾸어놓았다. visited가 있기 때문에 정상인이 헷갈리는 일은 없을 것임
# 적록색맹의 시점으로 볼 때는 녹색의 경우의 수를 완전히 빼고 이중 for문을 돌았다.
# 최대한 하나의 함수로 작성하고자 노력했는데, 재귀 깊이가 꽤 깊은 이중 for문을 두 번 돌리는 일은 별로 좋아보이지 않음
# 좋은 방법을 찾아봐야겠다

import sys
sys.setrecursionlimit(5000000)

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(input()))

d_x = [-1, 1, 0, 0]
d_y = [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]


def inRange(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y, color):
    if not inRange(x, y):
        return False
    if grid[x][y] == color and visited[x][y] == False:
        visited[x][y] = True
        if color == 'G':
            grid[x][y] = 'R'
        for i in range(4):
            new_x, new_y = x + d_x[i], y + d_y[i]
            dfs(new_x, new_y, color)
        return True
    return False


count = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            if dfs(i, j, 'R'):
                count += 1
        elif grid[i][j] == 'G':
            if dfs(i, j, 'G'):
                count += 1
        else:
            if dfs(i, j, 'B'):
                count += 1

visited = [[False] * n for _ in range(n)]
count_diff = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            if dfs(i, j, 'R'):
                count_diff += 1
        else:
            if dfs(i, j, 'B'):
                count_diff += 1


print(count, count_diff)
