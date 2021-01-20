def maxRec(n, m, grid):
    count_all = []
    count_max = []
    max_val = 0
    for row in range(0, n):
        for col in range(0, m):
            for i in range(n):
                for j in range(m):
                    count = 0
                    for k in range(i, i+row+1):
                        for l in range(j, j+col+1):
                            if k+row >= n or l+col >= m:
                                continue
                            if grid[k][l] < 0:
                                count = -1
                                break
                            else:
                                count += 1
                    if count == -1:
                        continue
                    count_all.append(count)
            max_val = max(count_all)
            count_max.append(max_val)
            print(count_max)
    max_count_val = max(count_max)

    return max_count_val


n, m = input().split()
n, m = int(n), int(m)
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
count_max = maxRec(n, m, grid)
print(count_max)
# print(max(count_max))
