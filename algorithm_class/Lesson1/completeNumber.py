import math


def findCompleteNumber(s, e):
    count = 0
    for i in range(s, e+1):
        num = 1
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                num += j
            if i % (i//j) == 0:
                num += (i//j)
        if num == i:
            count += 1
    print(count)


s, e = input().split()
s, e = int(s), int(e)
findCompleteNumber(s, e)
