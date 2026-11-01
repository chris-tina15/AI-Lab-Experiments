
# Experiment 2: DFS for Dependency and Reachability Analysis

# Represent the AI deployment pipeline as a directed graph
pipeline = {
    "A": ["B", "C", "D"],
    "B": ["E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["H"],
    "F": ["H"],
    "G": ["H"],
    "H": ["L"],
    "L": []
}

def dfs(graph, start, goal):
    visited = set()
    parent = {start: None}
    traversal = []

    def visit(node):
        visited.add(node)
        traversal.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                visit(neighbor)

    # Perform DFS traversal
    visit(start)

    print("\n--- DFS RESULT ---")
    print("DFS Traversal Order:", traversal)

    if goal not in visited:
        print("Target is not reachable.")
        return

    # Reconstruct a valid path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Target is reachable.")
    print("Valid Path:", " -> ".join(path))


# Accept user input
start = input(
    "Enter starting task (A, B, C, D, E, F, G, H, L): "
).strip().upper()

goal = input(
    "Enter target task (A, B, C, D, E, F, G, H, L): "
).strip().upper()

if start not in pipeline or goal not in pipeline:
    print("Invalid task. Please enter a valid node.")
else:
    dfs(pipeline, start, goal)
