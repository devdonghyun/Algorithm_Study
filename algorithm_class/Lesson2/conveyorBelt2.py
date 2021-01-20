def conveyorBelt(n, t, list1, list2):
    for _ in range(t):
        tmp = list1[-1]
        for i in range(n-1, 0, -1):
            list1[i] = list1[i-1]
        list1[0] = list2[n-1]

        for i in range(n-1, 0, -1):
            list2[i] = list2[i-1]
        list2[0] = tmp


n, t = input().split()
n, t = int(n), int(t)
list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]
conveyorBelt(n, t, list1, list2)
print(' '.join(str(x) for x in list1))
print(' '.join(str(x) for x in list2))
