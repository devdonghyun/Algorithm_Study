n, m = map(int, input().split())
x, y, d = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
visited = [[0] * m for _ in range(n)]


def turnLeft():
    global d
    global turn_count
    d -= 1
    turn_count += 1
    if d == -1:
        d = 3


d_x = [-1, 0, 1, 0]
d_y = [0, 1, 0, -1]
#      북, 동, 남, 서
visited[x][y] = 1
turn_count = 0
count = 1
while True:
    turnLeft()
    new_x, new_y = x + d_x[d], y + d_y[d]
    if grid[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
        visited[new_x][new_y] = 1
        count += 1
        turn_count = 0
        x, y = new_x, new_y
    else:
        if turn_count == 4:
            new_x, new_y = x - d_x[d], y - d_y[d]
            if grid[new_x][new_y] == 1:
                break
            else:
                x, y = new_x, new_y
                turn_count = 0

print(count)
