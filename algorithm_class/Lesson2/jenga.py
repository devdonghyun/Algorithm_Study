def playJenga(n, jenga, s, e):
    idx = s-1
    end = e-1
    while True:
        jenga[idx] = 0
        if idx == end:
            break
        idx += 1

    temp = []
    for i in range(len(jenga)):
        if jenga[i] != 0:
            temp.append(jenga[i])
    jenga = temp

    return jenga


n = int(input())
jenga = []
for i in range(n):
    jenga.append(int(input()))
f1, f2 = input().split()
f1, f2 = int(f1), int(f2)
s1, s2 = input().split()
s1, s2 = int(s1), int(s2)

jenga = playJenga(n, jenga, f1, f2)
jenga = playJenga(n, jenga, s1, s2)

print(len(jenga))
for val in jenga:
    print(val)
