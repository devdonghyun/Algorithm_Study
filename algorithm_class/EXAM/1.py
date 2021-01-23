n, m = input().split()
n, m = int(n), int(m)

x, y, d = input().split()
x, y, d = int(x), int(y), int(d)

grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
