def initialize():
    DP.append(0)
    for _ in range(1, n+1):
        DP.append(-float('inf'))


def LIS():
    initialize()
    for i in range(1, n+1):
        for j in range(0, i):
            if lis_list[i] > lis_list[j]:
                DP[i] = max(DP[i], DP[j] + 1)


n = int(input())
lis_list = [int(x) for x in input().split()]
lis_list.insert(0, 0)
DP = []
LIS()
print(max(DP))
