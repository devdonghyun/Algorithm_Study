def initialize():
    DP[0][0] = grid[0][0]
    for i in range(1, n):
        DP[i][0] = DP[i-1][0] + grid[i][0]
        DP[0][i] = DP[0][i-1] + grid[0][i]


def maxSquareRoute():
    initialize()

    for i in range(1, n):
        for j in range(1, n):
            DP[i][j] = max(DP[i-1][j] + grid[i][j], DP[i][j-1] + grid[i][j])


n = int(input())
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
DP = [
    [-float('inf') for _ in range(n)]
    for _ in range(n)
]
maxSquareRoute()
print(DP[n-1][n-1])
