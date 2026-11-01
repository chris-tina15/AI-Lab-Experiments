
# Experiment 6: Map Colouring Using CSP and Backtracking

# Define regions and their neighbouring regions
regions = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D", "F"],
    "F": ["D", "E"]
}

# Available colours (domain)
colours = ["Red", "Green", "Blue"]

# Stores the assigned colour for each region
assignment = {}
assignment_attempts = 0


def is_valid(region, colour):
    # Check whether neighbouring regions have different colours
    for neighbour in regions[region]:
        if assignment.get(neighbour) == colour:
            return False

    return True


def solve_csp(index=0):
    global assignment_attempts

    region_list = list(regions.keys())

    # All regions have been assigned colours
    if index == len(region_list):
        return True

    region = region_list[index]

    for colour in colours:
        assignment_attempts += 1

        if is_valid(region, colour):
            assignment[region] = colour

            if solve_csp(index + 1):
                return True

            # Backtrack
            del assignment[region]

    return False


print("--- MAP COLOURING RESULT ---")

if solve_csp():
    for region in regions:
        print(f"Region {region}: {assignment[region]}")

    # Verify all adjacency constraints
    valid = all(
        assignment[region] != assignment[neighbour]
        for region in regions
        for neighbour in regions[region]
    )

    print("\nAll adjacency constraints satisfied:", valid)
    print("Assignment attempts:", assignment_attempts)

else:
    print("No valid colouring exists.")
