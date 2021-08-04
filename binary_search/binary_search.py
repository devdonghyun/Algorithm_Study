# 이진 탐색 알고리즘 구현

def binarySearch(t, s, e):

    if s > e:
        return None

    m = (s+e)//2

    if array[m] == t:
        return m
    elif array[m] > t:
        return binarySearch(t, s, m-1)
    else:
        return binarySearch(t, m+1, e)


array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
result = binarySearch(4, 0, len(array)-1)
if result == None:
    print("Not Found")

else:
    print(result+1)
