def ATM(n, t):
    t.sort()
    for i in range(1, n):
        t[i] += t[i-1]
    return sum(t)


n = int(input())
t = [int(x) for x in input().split()]
print(ATM(n, t))
