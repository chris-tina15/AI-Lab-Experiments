
# Experiment 3: Water Jug Problem Using BFS
from collections import deque

CAP_A = 4
CAP_B = 3

def get_next_states(state):
    a, b = state
    result = []

    def add(action, x, y):
        new_state = (x, y)
        if new_state != state:
            result.append((action, new_state))

    # Fill either jug
    add("Fill 4L jug", CAP_A, b)
    add("Fill 3L jug", a, CAP_B)

    # Empty either jug
    add("Empty 4L jug", 0, b)
    add("Empty 3L jug", a, 0)

    # Pour 4L jug into 3L jug
    amount = min(a, CAP_B - b)
    add("Pour 4L -> 3L", a - amount, b + amount)

    # Pour 3L jug into 4L jug
    amount = min(b, CAP_A - a)
    add("Pour 3L -> 4L", a + amount, b - amount)

    return result


def solve_water_jug():
    start = (0, 0)
    queue = deque([start])

    # Store previous states to reconstruct the solution
    parent = {start: None}
    action_used = {}
    goal = None

    while queue:
        state = queue.popleft()

        # Goal: exactly 2 litres in the 4L jug
        if state[0] == 2:
            goal = state
            break

        for action, next_state in get_next_states(state):
            if next_state not in parent:
                parent[next_state] = state
                action_used[next_state] = action
                queue.append(next_state)

    print("\n--- WATER JUG RESULT ---")

    if goal is None:
        print("No solution found.")
        return

    # Reconstruct the sequence of states
    solution = []
    current = goal

    while current is not None:
        solution.append(current)
        current = parent[current]

    solution.reverse()

    print("Initial state:", solution[0])

    for i in range(1, len(solution)):
        state = solution[i]
        print(f"Step {i}: {action_used[state]} -> {state}")

    print("Goal state:", goal)
    print("Total operations:", len(solution) - 1)


solve_water_jug()
