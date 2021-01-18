def inRange(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


def zigzagNum(grid, n, m):
    d_x, d_y = [1, 0, -1, 0], [0, 1, 0, 1]
    curr_dir, num = 0, 0
    x, y = 0, 0
    while True:
        if num == n*m:
            break

        grid[x][y] = num
        num += 1

        new_x, new_y = x + d_x[curr_dir], y + d_y[curr_dir]
        if not inRange(new_x, new_y):
            curr_dir += 1
            new_x, new_y = x + d_x[curr_dir], y + d_y[curr_dir]

        x, y = new_x, new_y
        print(grid)


n, m = input().split()
n, m = int(n), int(m)
grid = [
    [0 for _ in range(m)]
    for _ in range(n)
]
zigzagNum(grid, n, m)
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()
