import heapq


def ucs(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start, []))
    explored = set()

    while frontier:
        (cost, node, path) = heapq.heappop(frontier)
        if node not in explored:
            explored.add(node)
            path = path + [node]

            if node == goal:
                return path, cost

            for neighbor, edge_cost in graph[node].items():
                if neighbor not in explored:
                    heapq.heappush(frontier, (cost + edge_cost, neighbor, path))

    return None


# Example graph map
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 8, 'E': 10},
    'D': {'F': 2},
    'E': {'J': 6},
    'F': {'G': 3},
    'G': {'H': 4, 'I': 5},
    'H': {'J': 7},
    'I': {'J': 4},
    'J': {}
}

# Test the algorithm to find a path from A to J
path, cost = ucs(graph, 'A', 'J')
print("Path:", path)
print("Cost:", cost)
