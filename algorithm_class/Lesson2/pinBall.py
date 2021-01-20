def inRange(x, y):
    return 0 <= x < n and 0 <= y < n


def playGame(n, dirc, d_x, d_y):
    count_lst = []
    for i in range(n):
        curr_dir, count = 0, 0
        if dirc == 0:
            y = 0
            x = i
        elif dirc == 1:
            y = i
            x = 0
        elif dirc == 2:
            y = 0
            x = n-1-i
        else:
            y = n-1-i
            x = 0
        while True:
            new_x, new_y = x + d_x[curr_dir], y + d_y[curr_dir]
            if not inRange(new_x, new_y):
                count += 1
                count_lst.append(count)
                break
            count += 1
            if grid[x][y] == 1:
                curr_dir = 1
            if grid[x][y] == 2:
                curr_dir = 2
            x, y = new_x, new_y
    return count_lst


def pinBall(n, grid):
    count_all = []
    for dirc in range(4):
        if dirc == 0:
            d_x, d_y = [0, -1, 1], [1, 0, 0]
            count_row = playGame(n, dirc, d_x, d_y)
            count_all.append(count_row)
        elif dirc == 1:
            d_x, d_y = [1, 0, 0], [0, -1, 1]
            count_row = playGame(n, dirc, d_x, d_y)
            count_all.append(count_row)
        elif dirc == 2:
            d_x, d_y = [0, 1, -1], [-1, 0, 0]
            count_row = playGame(n, dirc, d_x, d_y)
            count_all.append(count_row)
        else:
            d_x, d_y = [-1, 0, 0], [0, 1, -1]
            count_row = playGame(n, dirc, d_x, d_y)
            count_all.append(count_row)
    return count_all


n = int(input())
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
count_all = pinBall(n, grid)
max_count = 0

print(count_all)

for i in range(4):
    for j in range(n):
        if count_all[i][j] > max_count:
            max_count = count_all[i][j]
print(max_count)
