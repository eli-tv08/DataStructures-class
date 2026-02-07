def DFS(graph, start, visited):
    visited[start] = True
    for ne in graph[start]:
        if not visited.get(ne, False):
            DFS(graph, ne, visited)
