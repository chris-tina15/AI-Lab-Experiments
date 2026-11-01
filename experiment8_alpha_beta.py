
# Experiment 8: Implementing Alpha-Beta Pruning

# Game tree with multiple possible moves and terminal utilities
game_tree = {
    "A": ["B", "C", "D"],

    "B": ["E", "F", "G"],
    "C": ["H", "I", "J"],
    "D": ["K", "L", "M"],

    "E": [3, 5],
    "F": [6, 9],
    "G": [1, 2],

    "H": [4, 6],
    "I": [7, 8],
    "J": [9, 10],

    "K": [1, 3],
    "L": [12, 14],
    "M": [15, 18]
}

nodes_evaluated = 0
leaves_evaluated = 0
branches_pruned = 0


def alpha_beta(node, alpha, beta, maximizing):
    global nodes_evaluated, leaves_evaluated, branches_pruned

    nodes_evaluated += 1

    # Return terminal utility
    if isinstance(node, int):
        leaves_evaluated += 1
        return node

    children = game_tree[node]

    if maximizing:
        value = float("-inf")

        for i, child in enumerate(children):
            child_value = alpha_beta(
                child, alpha, beta, False
            )
            value = max(value, child_value)
            alpha = max(alpha, value)

            # Prune remaining children when possible
            if alpha >= beta:
                branches_pruned += len(children) - i - 1
                break

        return value

    else:
        value = float("inf")

        for i, child in enumerate(children):
            child_value = alpha_beta(
                child, alpha, beta, True
            )
            value = min(value, child_value)
            beta = min(beta, value)

            # Prune remaining children when possible
            if alpha >= beta:
                branches_pruned += len(children) - i - 1
                break

        return value


# Evaluate root A as the maximizing player
best_value = alpha_beta(
    "A",
    float("-inf"),
    float("inf"),
    True
)

# Determine which root move has the best minimax value
root_values = {}

for child in game_tree["A"]:
    root_values[child] = min(
        alpha_beta(
            grandchild,
            float("-inf"),
            float("inf"),
            True
        )
        for grandchild in game_tree[child]
    )

best_move = max(root_values, key=root_values.get)

print("--- ALPHA-BETA PRUNING RESULT ---")
print("Root move values:", root_values)
print("Best move for AI:", best_move)
print("Optimal utility value:", best_value)
print("Nodes evaluated:", nodes_evaluated)
print("Terminal nodes evaluated:", leaves_evaluated)
print("Branches pruned:", branches_pruned)
