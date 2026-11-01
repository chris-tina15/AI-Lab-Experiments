
from collections import deque

hospital = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B", "G"],
    "E": ["B", "C", "F"],
    "F": ["E", "H"],
    "G": ["D", "H"],
    "H": ["F", "G"]
}

def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    explored = []

    while queue:
        node = queue.popleft()
        explored.append(node)

        if node == goal:
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    if goal not in parent:
        print("No route exists.")
        return

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Shortest route:", " -> ".join(path))
    print("Corridors traversed:", len(path) - 1)
    print("Nodes explored:", len(explored))
    print("Exploration order:", explored)

start = input("Enter source node (A-H): ").strip().upper()
goal = input("Enter destination node (A-H): ").strip().upper()

if start not in hospital or goal not in hospital:
    print("Invalid node.")
else:
    bfs(hospital, start, goal)
