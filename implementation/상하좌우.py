def inRange(x, y):
    if 1 <= x <= n and 1 <= y <= n:
        return True
    else:
        return False


def goTravel():
    d_x = [0, 0, -1, 1]
    d_y = [-1, 1, 0, 0]

    s_x, s_y = 1, 1
    for direc in path:
        if direc == "L":
            direc_num = 0
        elif direc == "R":
            direc_num = 1
        elif direc == "U":
            direc_num = 2
        else:
            direc_num = 3
        new_x, new_y = s_x + d_x[direc_num], s_y + d_y[direc_num]
        if inRange(new_x, new_y):
            s_x, s_y = new_x, new_y

    print(s_x, s_y)


n = int(input())
path = input().split()
goTravel()
