def zigzagNum(grid, n, m):
    d_x = [1, -1]
    curr_dir, num = 0, 0
    x, y = 0, 0

    while True:
        if num == n*m:
            break

        grid[x][y] = num
        num += 1

        x += d_x[curr_dir]

        if x >= n or x < 0:
            x -= d_x[curr_dir]
            if curr_dir == 0:
                curr_dir = 1
            else:
                curr_dir = 0
            y += 1
            if y >= m or y < 0:
                break


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
