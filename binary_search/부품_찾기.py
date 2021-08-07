# 이것이 코딩테스트다 - 이진탐색 -> 부품 찾기 (10분)
# 이진 탐색을 이용하여 고객이 요청하는 물품이 가게에 있는지 찾는 문제
# 이진 탐색을 이용하면서 정렬을 하지 않는 실수를 했다


n = int(input())
store = list(map(int, input().split()))
m = int(input())
custom = list(map(int, input().split()))


def binarySearch(array, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binarySearch(array, target, start, mid-1)
    else:
        return binarySearch(array, target, mid+1, end)


store.sort()
for num in custom:
    if binarySearch(store, num, 0, len(store)-1):
        print("yes", end=' ')
    else:
        print("no", end=' ')
