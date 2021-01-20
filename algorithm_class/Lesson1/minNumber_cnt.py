import sys
INT_MAX = sys.maxsize


def minNumber(n, num):
    min_val = INT_MAX
    count = 0
    for i in range(n):
        if min_val > num[i]:
            min_val = num[i]
            count = 1
        elif min_val == num[i]:
            count += 1

    print(min_val, count)


n = int(input())
num = [int(x) for x in input().split()]
minNumber(n, num)
