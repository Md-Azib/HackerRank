def k(l):
    return l[0]


g_nodes, g_edges = map(int, input().split())
graph = []

for i in range(g_edges):
    temp = list(map(int, input().split()))
    a, b, w = temp[0], temp[1], temp[2]
    graph.append([w, a, b])
    #graph.append([w, b, a])
graph = sorted(graph, key=k)
print(graph)
components = []
for i in range(len(graph)):
    components.append(i)
weight = 0
mst = []
mst.append(graph[0])
print(mst)
for i in range(1, len(graph)):
    for j in range(i + 1, len(graph)):
        if graph[i][1:3] == graph[j][1:3] or graph[i][1:3].reverse() == graph[j][1:3]:
            components[i] = components[j]
    if components[i] != components[0]:
        components[i] = 0
        mst.append(graph[i])
print(mst)
print(weight)








