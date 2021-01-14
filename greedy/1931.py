def castClass(T):
    L = [0]
    k = 0
    for i in range(1, n):
        if T[k][1] <= T[i][0]:
            L.append(i)
            k = i
    return len(L)


n = int(input())
T = []
for i in range(n):
    s, f = input().split()
    s, f = int(s), int(f)
    T.append((s, f))
T = sorted(T, key=lambda x: x[0])
T = sorted(T, key=lambda x: x[1])
print(castClass(T))

# (2,2), (1,2) 형태이 입력으로 수업이 있을 때 끝나는 시간만으로 정렬을 하면
# (2,2) 수업이 끝난 시간보다 (1,2) 수업이 시작하는 시간이 작아서 (1,2)는 선택되지 못 한다.
# 그러나 문제 조건에서 (1,2), (2,2) 모두 채택 가능하다. (시작 시간과 끝나는 시간이 같을 수도 있다고 한다)
# 따라서 시작 시간으로 우선 정렬 후 끝나는 시간으로 정렬하여
# 시작 시간으로 정렬된 순서를 유지하려는 경향성을 가져간다.
# 다시 풀어볼 수 있도록 하자.
