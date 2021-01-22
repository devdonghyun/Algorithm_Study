
def countBST(n):
    if n == 1:
        DP[1] = 1
        return
    DP[2] = 2
    for i in range(3, n+1):
        DP[i] = i + DP[i-1]


n = int(input())
DP = [0 for _ in range(n+1)]
countBST(n)
print(DP[n])
