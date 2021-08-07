# 이것이 코딩테스트다 - 이진탐색 -> 떡볶이 떡 만들기
# 아진 탐색 알고리즘을 써야한다는 생각에 사로잡혀서 리스트 안에서 이진탐색을 어떻게 쓸지만 고민했다
# 정작 해결방법은 칼의 높이를 이진 탐색을 이용해 찾는 것이었다


n, m = map(int, input().split())
heights = list(map(int, input().split()))


def findKnife():
    result = 0
    start = 0
    end = max(heights)
    while start <= end:
        mid = (start+end)//2
        sum_height = 0

        for h in heights:
            if mid < h:
                sum_height += (h-mid)

        if sum_height < m:
            end = mid-1
        else:
            result = mid
            start = mid+1

    return result


print(findKnife())
