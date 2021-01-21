def selectOne(cnt):
    if cnt == n:
        for i in range(len(ans)):
            print(ans[i], end=' ')
        print()
        return
    for i in range(1, k+1):
        if cnt >= 3:
            count = 0
            for j in range(1, 3):
                if ans[cnt-j] == i:
                    count += 1
            if count == 2:
                continue
            else:
                ans.append(i)
                selectOne(cnt+1)
                ans.pop()
        else:
            ans.append(i)
            selectOne(cnt+1)
            ans.pop()


k, n = input().split()
k, n = int(k), int(n)
ans = []
selectOne(0)
