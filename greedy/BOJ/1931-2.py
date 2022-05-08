# 백준 1931
# 실버 1
# 2022-05-03 다시 풀어봄

def getRoom(n):
    result_list = [time_list[0]]
    for i in range(1, n):
        if result_list[-1][1] <= time_list[i][0]:
            result_list.append(time_list[i])

    return len(result_list)


n = int(input())
time_list = []
for _ in range(n):
    s, e = map(int, input().split())
    time_list.append((s, e))

time_list.sort(key=lambda x: x[0])
time_list.sort(key=lambda x: x[1])

print(getRoom(n))
