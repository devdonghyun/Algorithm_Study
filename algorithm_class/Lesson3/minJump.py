def calMinJump(idx, cnt):
    if idx == n-1:
        count_jump.append(cnt)
        return
    if idx > n-1:
        return
    for i in range(jump[idx]):
        calMinJump(idx+i+1, cnt+1)


n = int(input())
jump = [int(x) for x in input().split()]
count_jump = []
idx, cnt = 0, 0
calMinJump(idx, cnt)
if len(count_jump) == 0:
    print(-1)
else:
    print(min(count_jump))
