# 백준 dfs - 2667번: 단지 번호 붙이기
# 이것이 코딩테스트다 dfs 미로 탈출 예제의 아이디어를 사용
# 이 풀이 방법은 뭔가 찜찜한 부분이 있음
# 이전의 풀이 방법으로 다시 풀어보자

n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input())))

d_x = [-1, 1, 0, 0]
d_y = [0, 0, -1, 1]


def inRange(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False


def dfs(x, y):
    global count
    if not inRange(x, y):
        return False
    if grid[x][y] == 1:
        count += 1
        grid[x][y] = 0
        for i in range(4):
            new_x, new_y = x + d_x[i], y + d_y[i]
            dfs(new_x, new_y)

        return True
    return False


count_list = []
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j) == True:
            count_list.append(count)

count_list.sort()
print(len(count_list))
for num in count_list:
    print(num)
