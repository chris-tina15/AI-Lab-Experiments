
# Experiment 4: A* Search for Intelligent Route Planning
import heapq
from itertools import count

# Weighted graph representing delivery routes
graph = {
    "A": {"B": 4, "C": 3},
    "B": {"A": 4, "C": 2, "D": 5},
    "C": {"A": 3, "B": 2, "D": 6, "E": 4},
    "D": {"B": 5, "C": 6, "E": 1, "F": 2},
    "E": {"C": 4, "D": 1, "F": 3},
    "F": {"D": 2, "E": 3}
}

# Heuristic estimates from the lab document
heuristic = {
    "A": 6,
    "B": 4,
    "C": 5,
    "D": 2,
    "E": 3,
    "F": 0
}

def a_star(graph, start, goal):
    tie_breaker = count()

    # Priority queue: f-score, tie-breaker, node, g-score
    frontier = [
        (heuristic[start], next(tie_breaker), start, 0)
    ]

    g_cost = {start: 0}
    parent = {start: None}
    expanded = []

    while frontier:
        f, _, node, cost = heapq.heappop(frontier)

        # Ignore outdated entries
        if cost != g_cost[node]:
            continue

        expanded.append(node)

        if node == goal:
            path = []
            current = goal

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("\n--- A* SEARCH RESULT ---")
            print("Optimal route:", " -> ".join(path))
            print("Total path cost:", g_cost[goal])
            print("Node expansion order:", expanded)
            return

        for neighbor, edge_cost in graph[node].items():
            new_cost = g_cost[node] + edge_cost

            if new_cost < g_cost.get(neighbor, float("inf")):
                g_cost[neighbor] = new_cost
                parent[neighbor] = node

                f_score = new_cost + heuristic[neighbor]

                heapq.heappush(
                    frontier,
                    (
                        f_score,
                        next(tie_breaker),
                        neighbor,
                        new_cost
                    )
                )

    print("No route exists.")


start = input("Enter starting node (A-F): ").strip().upper()
goal = input("Enter destination node (A-F): ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid node. Enter A, B, C, D, E or F.")
else:
    a_star(graph, start, goal)
