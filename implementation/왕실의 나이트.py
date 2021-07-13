pos = input()
row = [" ", "a", "b", "c", "d", "e", "f", "g", "h"]
x, y = row.index(pos[0]), int(pos[1])


def inRange(x, y):
    if 1 <= x <= 8 and 1 <= y <= 8:
        return True
    else:
        return False


d_x = [2, 2, -2, -2, 1, -1, 1, -1]
d_y = [1, -1, 1, -1, 2, 2, -2, -2]
count = 0

for i in range(8):
    new_x, new_y = x + d_x[i], y + d_y[i]
    if inRange(new_x, new_y):
        count += 1

print(count)
