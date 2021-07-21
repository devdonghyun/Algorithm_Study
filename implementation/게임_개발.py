
def turnLeft():
    global d
    d -= 1
    if d == -1:
        d = 3


def findPath(x, y):

    count = 1
    turn_time = 0
    d_x = [0, 1, 0, -1]
    d_y = [-1, 0, -1, 0]
    #      북, 동, 남, 서
    visited[x][y] = 1
    while True:
        turnLeft()
        new_x, new_y = x + d_x[d], y + d_y[d]
        if grid[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
            count += 1
            visited[new_x][new_y] = 1
            x, y = new_x, new_y
            turn_time = 0
            continue
        else:
            turn_time += 1

        if turn_time == 4:
            new_x, new_y = x - d_x[d], y - d_y[d]
            if grid[new_x][new_y] == 0:
                x, y = new_x, new_y
            else:
                break

            turn_time = 0

    print(count)


n, m = map(int, input().split())
x, y, d = map(int, input().split())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]
# visited = [[0] * m for _ in range(n)]
findPath(x, y)
