# 백준 1715
# 골드 4
# 2022-05-03


import heapq


def minCardCompare(n):

    if len(card_heap) == 1:
        return 0
    else:
        result = 0
        while len(card_heap) > 1:
            firstMin = heapq.heappop(card_heap)
            secondMin = heapq.heappop(card_heap)
            compareCount = firstMin + secondMin
            result += compareCount
            heapq.heappush(card_heap, compareCount)

        return result


n = int(input())
card_heap = []
for _ in range(n):
    heapq.heappush(card_heap, int(input()))

print(minCardCompare(n))

# 10 20 25 27 35
# 30 25 27 35 -> 30

# 25 27 30 35
# 52 30 35 -> 52

# 30 35 52
# 65 52 -> 65

# 117 -> 117
