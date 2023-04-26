def dfs(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path.append(start)
    if start == end:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, end, visited, path)
            if new_path:
                return new_path
    path.pop()


graph = {
    'A': ['B', 'G'],
    'B': ['C', 'F', 'A'],
    'C': ['E', 'B'],
    'D': ['E'],
    'E': ['I', 'D','C'],
    'F': ['J', 'G', 'B'],
    'G': ['F', 'A'],
    'H': ['I'],
    'I': ['H','J','K'],
    'J': ['I','F'],
    'k': ['I']
}

path = dfs(graph, 'A', 'J')
print(path)
