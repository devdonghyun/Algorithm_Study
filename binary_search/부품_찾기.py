
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


for num in custom:
    if binarySearch(store, num, 0, len(store)-1):
        print("yes", end=' ')
    else:
        print("no", end=' ')
