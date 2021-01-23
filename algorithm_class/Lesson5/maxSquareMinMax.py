def initialize():
    DP[0][0] = grid[0][0]
    for i in range(1, n):
        if grid[i][0] <= grid[i-1][0]:
            DP[i][0] = grid[i][0]
        else:
            DP[i][0] = DP[i-1][0]

        if grid[0][i] <= grid[0][i-1]:
            DP[0][i] = grid[0][i]
        else:
            DP[0][i] = DP[0][i-1]


def maxSquareMinMax():
    initialize()
    for i in range(1, n):
        for j in range(1, n):
            if grid[i][j] <= max(DP[i-1][j], DP[i][j-1]):
                DP[i][j] = grid[i][j]
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])


n = int(input())
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
DP = [
    [float('inf') for _ in range(n)]
    for _ in range(n)
]
maxSquareMinMax()
for i in range(n):
    print(DP[i])
print(DP[n-1][n-1])
