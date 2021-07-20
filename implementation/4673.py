
# 백준 구현 4673번
# 반복문 한 개로 해결할 수는 없을까?
# 두 번째 반복문에서 시간을 줄일 수 있는 방법은 없을까?

num_list = []
for i in range(1, 10001):
    strInt = str(i)
    for num in strInt:
        i += int(num)
    num_list.append(i)

for i in range(1, 10001):
    if i in num_list:
        continue
    print(i)
