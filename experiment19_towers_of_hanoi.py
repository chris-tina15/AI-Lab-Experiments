
move_count = 0

def tower_of_hanoi(n, source, auxiliary, destination):
    global move_count

    if n == 1:
        move_count += 1

        print(
            "Move disk 1 from",
            source,
            "to",
            destination
        )
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(
        n - 1,
        source,
        destination,
        auxiliary
    )

    # Move the largest disk to destination
    move_count += 1

    print(
        "Move disk", n,
        "from", source,
        "to", destination
    )

    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(
        n - 1,
        auxiliary,
        source,
        destination
    )


# Main program
n = 3

print("Towers of Hanoi")
print("----------------")
print("Number of disks:", n)

print("\nSequence of moves:")

tower_of_hanoi(n, 'A', 'B', 'C')

print("\nTotal Moves:", move_count)
print("Minimum Moves Required:", 2**n - 1)
