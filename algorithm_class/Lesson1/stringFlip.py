def stringFlip(s, q, req):
    for i in range(q):
        if req[i] == 1:
            s = s[1:]+s[:1]
        elif req[i] == 2:
            s = s[-1:]+s[:-1]
        elif req[i] == 3:
            s = s[::-1]
        print(s)


s, q = input().split()
q = int(q)
req = []
for i in range(q):
    req.append(int(input()))
stringFlip(s, q, req)
