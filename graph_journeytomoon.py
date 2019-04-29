def dfs(root):
    visited[root] = True
    for i in graph:
        for j in graph[i]:
            print(j, end=' ')
            if not visited[j]:
                print()
                dfs(j)



n, p = map(int, input().split())
graph = {}
visited = {}
for i in range(n):
    graph[i] = []
    visited[i] = False
for i in range(p):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[0] = True
dfs(0)
print(visited)
print(graph)
