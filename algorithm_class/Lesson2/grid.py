def inRange(x, y):
    return 0 <= x < n and 0 <= y < n


def biggerGrid(n, curr_x, curr_y, grid, max_val):
    d_x, d_y = [-1, 1, 0, 0], [0, 0, -1, 1]

    for curr_dir in range(4):
        new_x = curr_x + d_x[curr_dir]
        new_y = curr_y + d_y[curr_dir]

        if inRange(new_x, new_y) and grid[new_x][new_y] > max_val:
            curr_x, curr_y = new_x, new_y
            max_val = grid[new_x][new_y]
            return True, curr_x, curr_y, max_val

    return False, curr_x, curr_y, max_val


n, r, c = input().split()
n, r, c = int(n), int(r), int(c)
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
result = [grid[r-1][c-1]]
max_val = grid[r-1][c-1]
curr_x, curr_y = r-1, c-1
while True:
    result_bool, curr_x, curr_y, max_val = biggerGrid(
        n, curr_x, curr_y, grid, max_val)
    if result_bool == False:
        break
    else:
        result.append(grid[curr_x][curr_y])
print(' '.join(str(x) for x in result))
