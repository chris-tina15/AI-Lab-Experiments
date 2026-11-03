
from collections import deque

# Locations: 0 = A, 1 = B, 2 = C
# Banana is hanging at location C

initial_state = (0, 1, False, False)
goal_location = 2

# State: (monkey_position, box_position, on_box, has_banana)

def get_actions(state):
    monkey, box, on_box, has_banana = state
    actions = []

    if has_banana:
        return actions

    # Move monkey left or right
    if not on_box:
        for direction in [-1, 1]:
            new_position = monkey + direction

            if 0 <= new_position <= 2 and new_position != box:
                actions.append((
                    (new_position, box, False, False),
                    "Move to location " + str(new_position)
                ))

    # Push the box one step away from the monkey
    if not on_box and abs(monkey - box) == 1:
        direction = 1 if box > monkey else -1
        new_box_position = box + direction

        if 0 <= new_box_position <= 2:
            actions.append((
                (box, new_box_position, False, False),
                "Push the box to location " + str(new_box_position)
            ))

    # Climb onto the box
    if not on_box and abs(monkey - box) == 1 and box == goal_location:
        actions.append((
            (box, box, True, False),
            "Climb onto the box"
        ))

    # Grasp the banana
    if on_box and monkey == goal_location and box == goal_location:
        actions.append((
            (monkey, box, True, True),
            "Grasp the banana"
        ))

    return actions


def solve_monkey_problem():
    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        current_state, path = queue.popleft()

        if current_state[3]:
            return path

        for next_state, action in get_actions(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))

    return None


# Execute planning algorithm
solution = solve_monkey_problem()

print("Monkey and Banana Problem")
print("-------------------------")
print("Initial State: Monkey at A, Box at B")
print("Banana Location: C")

print("\nSequence of Actions:")

if solution:
    for step, action in enumerate(solution, 1):
        print("Step", step, ":", action)

    print("\nGoal Achieved: Monkey obtained the banana!")
    print("Total Actions:", len(solution))

else:
    print("No solution found.")
