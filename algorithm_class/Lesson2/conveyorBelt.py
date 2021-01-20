def conveyorBelt(t, lst):
    for _ in range(t):
        lst = lst[-1:] + lst[:-1]
    return lst


n, t = input().split()
n, t = int(n), int(t)
list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]
list2 = sorted(list2, reverse=True)
lst = list1 + list2
print(lst)
new_lst = conveyorBelt(t, lst)

print(' '.join(str(x) for x in new_lst[:n]))
print(' '.join(str(x) for x in new_lst[n:]))
