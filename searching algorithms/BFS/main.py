from collections import deque

# define the graph as a dictionary of nodes and their neighbors
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

def bfs(graph, start, goal):
    # create a queue for BFS
    queue = deque()
    # enqueue the starting node and its path
    queue.append([start])
    # keep track of visited nodes
    visited = set()

    while queue:
        # dequeue the first path from the queue
        path = queue.popleft()
        # get the last node from the path
        node = path[-1]

        # if the node has not been visited yet
        if node not in visited:
            # get the neighbors of the node
            neighbors = graph[node]
            # go through all neighbor nodes, construct a new path and
            # enqueue it to the queue
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                # if the neighbor is the goal, return the path
                if neighbor == goal:
                    return new_path

            # mark the node as visited
            visited.add(node)

    # if there is no path from start to goal
    return None

# test the program to find a path from A to J
path = bfs(graph, 'A', 'J')
print(path)
