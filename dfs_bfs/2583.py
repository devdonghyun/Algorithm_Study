# 백준 bfs - 2583번: 영역 구하기  <52분 20초>
# bfs로 풀기 위해 주어진 직사각형의 좌표를 이용해 2차원 리스트에 직사각형을 칠한다
# 위 아이디어를 생각하는데 조금 시간이 많이 걸림
# 나머지 bfs로 구현하는 것은 다른 문제와 유사하여 크게 문제가 없었음
# 애초에 입력 받을 때부터 직사각형을 칠할 수 있었는데 그 부분은 고칠 부분인 듯


from collections import deque

m, n, k = map(int, input().split())
coor = []

for _ in range(k):
    coor.append(list(map(int, input().split())))

grid = [[0] * n for _ in range(m)]
for a in range(k):
    s_x, s_y, e_x, e_y = coor[a][0], coor[a][1], coor[a][2], coor[a][3]
    for i in range(s_y, e_y):
        for j in range(s_x, e_x):
            grid[i][j] = 1

d_x = [-1, 1, 0, 0]
d_y = [0, 0, -1, 1]
visited = [[0] * n for _ in range(m)]


def inRange(x, y):
    return 0 <= x < m and 0 <= y < n


def bfs():
    count = 0
    while queue:
        x, y = queue.popleft()
        count += 1
        for i in range(4):
            new_x, new_y = x + d_x[i], y + d_y[i]
            if inRange(new_x, new_y) and grid[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
                grid[new_x][new_y] = grid[x][y] + 1
                visited[new_x][new_y] = 1
                queue.append((new_x, new_y))

    count_list.append(count)


queue = deque()
count_list = []
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            queue.append((i, j))
            count = 0
            bfs()

count_list.sort()
print(len(count_list))
for num in count_list:
    if num == 1:
        print(num, end=' ')
    else:
        print(num-1, end=' ')
