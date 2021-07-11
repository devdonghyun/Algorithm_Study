# def maxNumLaw():
#     sum = 0
#     count = 0
#     max_num = max(num)
#     num.remove(max_num)
#     sec_max = max(num)
#     if max_num == sec_max:
#         for i in range(m):
#             sum += max_num
#     else:
#         while (count < m):
#             for j in range(k):
#                 if count == m:
#                     break
#                 sum += max_num
#                 count += 1
#             if count == m:
#                 break
#             sum += sec_max
#             count += 1

#     return sum

def maxNumLaw():
    result = 0
    count = 0
    max_num = max(num)
    num.remove(max_num)
    sec_max = max(num)
    if max_num == sec_max:
        for i in range(m):
            result += max_num
    else:
        while (True):
            for j in range(k):
                if count == m:
                    break
                result += max_num
                count += 1
            if count == m:
                break
            result += sec_max
            count += 1

    return result


n, m, k = input().split()
n, m, k = int(n), int(m), int(k)
num = [int(x) for x in input().split()]
print(maxNumLaw())
