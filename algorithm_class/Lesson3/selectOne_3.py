def selectOne(cnt):
    if cnt == n:
        for i in range(len(ans)):
            print(ans[i], end=' ')
        print()
        return
    for i in range(1, k+1):
        if cnt == 0 or (cnt != 0 and i > ans[-1]):
            ans.append(i)
            selectOne(cnt+1)
            ans.pop()
        else:
            continue


k, n = input().split()
k, n = int(k), int(n)
ans = []
selectOne(0)
