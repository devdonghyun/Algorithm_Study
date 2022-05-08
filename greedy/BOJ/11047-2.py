# 백준 11047
# 실버 3
# 2022-05-02에 다시 풀어봄

def changeCoin(k):
    count = 0
    for value in value_list[::-1]:
        count += k // value
        k %= value
        if k == 0:
            return count

    return count


n, k = map(int, input().split())
value_list = []
for i in range(n):
    value_list.append(int(input()))

print(changeCoin(k))
