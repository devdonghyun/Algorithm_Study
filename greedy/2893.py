def sugar(n):

    quote_five = n // 5
    remain_five = n % 5
    quote_three = remain_five // 3
    remain_three = remain_five % 3
    if remain_three == 0:
        return (quote_five + quote_three)
    else:
        while 1:
            quote_five -= 1
            remain_five += 5
            if remain_five > n:
                return -1
            quote_three = remain_five // 3
            remain_three = remain_five % 3
            if remain_three == 0:
                return (quote_five + quote_three)
        return -1


n = int(input())
print(sugar(n))
