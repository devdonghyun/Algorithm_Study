def countCoin(n, k, A):
    count = 0
    while 1:
        if A[n-1] <= k:
            count += k // A[n-1]
            if k % A[n-1] == 0:
                return count
            k %= A[n-1]
        n -= 1
    return count


n, k = input().split()
n, k = int(n), int(k)
A = []
for i in range(n):
    a = int(input())
    A.append(a)
print(countCoin(n, k, A))
