def centrifugalForce(grid, n):
    num = 1
    coor = n // 2
    curr_dir = 0
    d_x, d_y = 0, 1
    cnt_x, cnt_y = 0, 0
    m_x, m_y = [0, -1, 0, 1], [1, 0, -1, 0]
    x, y = coor, coor

    while True:
        grid[x][y] = num
        num += 1

        if num == n**2+1:
            break

        x += m_x[curr_dir]
        y += m_y[curr_dir]
        cnt_x += m_x[curr_dir]
        cnt_y += m_y[curr_dir]

        print(cnt_x, cnt_y)
        print(d_x, d_y)
        if cnt_x == d_x and cnt_y == d_y:
            cnt_x, cnt_y = 0, 0
            curr_dir += 1
            if curr_dir == 4:
                curr_dir = 0

            if d_x == 0:
                tmp_x = -d_y
            else:
                tmp_x = 0
            if d_y == 0:
                if d_x < 0:
                    tmp_y = d_x-1
                else:
                    tmp_y = d_x+1
            else:
                tmp_y = 0
            d_x, d_y = tmp_x, tmp_y

        print(grid)


n = int(input())
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]
centrifugalForce(grid, n)
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()
