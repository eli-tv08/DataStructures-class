def BFS(graph, start):
    queue = [start]
    visited = set([start])
    while queue:
        vertex = queue.pop(0)
        for ne in graph[vertex]:
            if ne not in visited:
                visited.add(ne)
                queue.append(ne)
    return visited
