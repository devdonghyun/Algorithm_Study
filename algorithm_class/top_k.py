def top_k(num, n, m):
    num.sort()
    print(num[m-1])


n, m = input().split()
n, m = int(n), int(m)
num = [int(x) for x in input().split()]
top_k(num, n, m)
