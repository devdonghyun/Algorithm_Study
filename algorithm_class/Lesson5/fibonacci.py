def fibonacci(n):
    DP = []
    DP.append(1)
    DP.append(1)
    for i in range(2, n):
        DP.append(DP[i-1] + DP[i-2])
    return DP[-1]


n = int(input())
ans = fibonacci(n)
print(ans)
