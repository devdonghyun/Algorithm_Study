# 백준 dfs - 4963번: 섬의 개수
# 대각선까지도 한 묶음으로 본다는 것이 새로웠음
# 여러 테스트케이스를 한 번에 입력받는 것도 새로웠음
# 두 가지 이외에는 다른 dfs 문제와 유사한 문제


import sys
sys.setrecursionlimit(5000000)

d_x = [-1, 1, 0, 0, -1, -1, 1, 1]
d_y = [0, 0, -1, 1, -1, 1, -1, 1]


def inRange(x, y):
    return 0 <= x < h and 0 <= y < w


def dfs(x, y):
    if not inRange(x, y):
        return False
    if grid[x][y] == 1:
        grid[x][y] = 0
        for i in range(8):
            new_x, new_y = x + d_x[i], y + d_y[i]
            dfs(new_x, new_y)

        return True
    return False


count_list = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    grid = []
    for _ in range(h):
        grid.append(list(map(int, input().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                count += 1

    count_list.append(count)

for num in count_list:
    print(num)
