# if-else 구문은 필요 없음
# 가장 큰 수와 두 번째로 큰 수를 찾을 때 정렬을 이용하면 시간복잡도를 줄일 수 있었음
#

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
#         count = m % k
#         for i in range(count):
#             sum += sec_max
#         for i in range(m-count):
#             sum += max_num

#     return sum

def maxNumLaw():
    sum = 0
    count = 0
    max_num = max(num)
    num.remove(max_num)
    sec_max = max(num)

    count = m % k
    for i in range(count):
        sum += sec_max
    for i in range(m-count):
        sum += max_num

    return sum


# n, m, k = input().split()
# n, m, k = int(n), int(m), int(k)
n, m, k = map(int, input().split())
num = [int(x) for x in input().split()]
print(maxNumLaw())
