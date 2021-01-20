def position_33(n, grid):
    row, col, count, max_cnt = 0, 0, 0, 0
    for row in range(n):
        for col in range(n):
            if row+2 >= n or col+2 >= n:
                continue

            for i in range(row, row+3):
                for j in range(col, col+3):
                    if grid[i][j] == 1:
                        count += 1
            if max_cnt < count:
                max_cnt = count
            count = 0

    return max_cnt


n = int(input())
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
print(position_33(n, grid))
