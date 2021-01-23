def findHos():
    person, hospital = [], []
    dist = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                person.append((i, j))
            if grid[i][j] == 2:
                hospital.append((i, j))

    for i in range(len(person)):
        p_x, p_y = person[i]
        each = []
        for j in range(len(hospital)):
            h_x, h_y = hospital[j]
            val = abs(h_x-p_x) + abs(h_y-p_y)
            each.append(val)
        dist.append(each)

    lst = []

    for i in range(len(dist)):
        min_idx = dist[i].index(min(dist[i]))
        min_val = min(dist[i])
        lst.append((min_idx, min_val))
    print(lst)
    # lst = sorted(lst, key=lambda x: x[1])
    count = 0
    hos_idx = []
    hos_dist = []
    hos_idx.append(lst[0][0])
    hos_dist.append(lst[0][1])

    for i in range(1, len(lst)):
        if lst[i][0] not in hos_idx:
            count += 1
            hos_idx.append(lst[i][0])
        hos_dist.append(lst[i][1])
        if len(hos_dist) == m:
            break
    print(hos_idx)
    print(hos_dist)

    sum_val = 0
    for i in range(m):
        sum_val += hos_dist[i]
    print(sum_val)


n, m = input().split()
n, m = int(n), int(m)
grid = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    grid.append(row)
findHos()
