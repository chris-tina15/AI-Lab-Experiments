
# Experiment 7: Implementing the Minimax Algorithm

# Binary game tree with terminal utility values
game_tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [3, 5],
    "E": [2, 9],
    "F": [12, 5],
    "G": [23, 23]
}

evaluated_values = {}

def minimax(node, maximizing):
    # If node is a terminal utility value
    if isinstance(node, int):
        return node

    # Recursively evaluate child nodes
    values = [
        minimax(child, not maximizing)
        for child in game_tree[node]
    ]

    if maximizing:
        value = max(values)
    else:
        value = min(values)

    evaluated_values[node] = value
    return value


# Start with A as the maximizing player
best_value = minimax("A", True)

print("--- MINIMAX RESULT ---")
print("Evaluated node values:")

for node, value in evaluated_values.items():
    print(f"Node {node}: {value}")

# Select the best move for MAX at the root
best_move = max(
    game_tree["A"],
    key=lambda child: evaluated_values[child]
)

print("\nBest move for AI:", best_move)
print("Best utility value:", best_value)
