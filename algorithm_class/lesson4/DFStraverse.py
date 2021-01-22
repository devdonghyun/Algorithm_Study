
def DFS(vertex):
    global count
    for curr_v in range(1, n+1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            count += 1
            visited[curr_v] = 1
            DFS(curr_v)


n, m = input().split()
n, m = int(n), int(m)

graph = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    start, end = input().split()
    start, end = int(start), int(end)
    graph[start][end] = 1
    graph[end][start] = 1

root_vertex = 1
count = 0
visited[root_vertex] = 1
DFS(root_vertex)
print(count)
