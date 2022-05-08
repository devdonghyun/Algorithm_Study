# 설탕 배달
# 브론즈 1

def divSugar(n):

    k = n

    if n % 5 == 0:
        return n // 5

    count = 0
    while n-3 >= 0:
        n -= 3
        count += 1
        if n % 5 == 0:
            return count + n // 5

    if k % 3 == 0:
        return k // 3

    return -1


n = int(input())
print(divSugar(n))
