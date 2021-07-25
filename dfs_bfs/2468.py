# 백준 dfs - 2468번: 안전 영역  <17분 23초>
# 지금까지 푼 dfs 문제와 크게 다르지 않았다
# 문제에서 약간의 조건만 바꿔주면 되기에 큰 어려움이 없었다
# 좀 더 색다른 유형을 풀어봐야할 듯 하다.

import sys
sys.setrecursionlimit(5000000)

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

d_x = [-1, 1, 0, 0]
d_y = [0, 0, -1, 1]


def inRange(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y, h):
    if not inRange(x, y):
        return False
    if grid[x][y] >= h and visited[x][y] == 0:
        visited[x][y] = 1
        for i in range(4):
            new_x, new_y = x + d_x[i], y + d_y[i]
            dfs(new_x, new_y, h)
        return True
    return False


count_list = []
for h in range(1, 101):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j, h):
                count += 1
    count_list.append(count)

count_list.sort(reverse=True)
print(count_list[0])
