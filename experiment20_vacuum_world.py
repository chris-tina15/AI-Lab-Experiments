
# Define room conditions
rooms = {
    'A': 'Dirty',
    'B': 'Clean',
    'C': 'Dirty',
    'D': 'Dirty'
}

locations = ['A', 'B', 'C', 'D']

current_position = 0


# Simple reflex agent
def simple_reflex_agent(location, status):
    if status == 'Dirty':
        return 'Suck'

    return 'Move'


print("Simple Reflex Agent - Vacuum World")
print("-----------------------------------")
print("Initial Room Conditions:", rooms)

step = 1

while True:

    # Check whether all rooms are clean
    if all(status == 'Clean' for status in rooms.values()):
        print("\nAll rooms are clean!")
        print("Cleaning task completed.")
        break

    current_room = locations[current_position]
    current_status = rooms[current_room]

    action = simple_reflex_agent(
        current_room,
        current_status
    )

    print(
        "\nStep", step,
        "- Location:", current_room,
        "- Status:", current_status
    )

    # Execute action
    if action == 'Suck':
        rooms[current_room] = 'Clean'
        print("Action: Cleaning room", current_room)

    else:
        print("Action: Moving to next room")
        current_position = (
            current_position + 1
        ) % len(locations)

    step += 1


# Display final result
print("\nFinal Room Conditions:", rooms)
print("Total Actions Performed:", step - 1)
