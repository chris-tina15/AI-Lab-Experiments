
# Experiment 10: Resolution Refutation

# Knowledge base represented in CNF
clauses = [
    {"EnjoysLearning"},                 # C1
    {"HasFreeTime"},                    # C2
    {"NotEnjoysLearning", "Happy"},     # C3
    {"NotHasFreeTime", "Happy"}         # C4
]

goal = "Happy"

print("Resolution Refutation\n")
print("--- Knowledge Base (CNF) ---")

for i, clause in enumerate(clauses, start=1):
    print(f"C{i}: {' OR '.join(sorted(clause))}")

# Negate the goal
negated_goal = "Not" + goal
clauses.append({negated_goal})

print(f"\nNegated goal added: {negated_goal}")

def complement(literal):
    if literal.startswith("Not"):
        return literal[3:]
    return "Not" + literal

# Resolution process
known = {frozenset(c) for c in clauses}
new_clauses = set()
empty_clause_found = False

print("\n--- Resolution Steps ---")

while True:
    current = list(known)
    new_clauses = set()

    for i in range(len(current)):
        for j in range(i + 1, len(current)):

            c1 = set(current[i])
            c2 = set(current[j])

            for literal in c1:
                opposite = complement(literal)

                if opposite in c2:
                    resolvent = (
                        (c1 - {literal}) |
                        (c2 - {opposite})
                    )

                    print(
                        f"Resolve {sorted(c1)} and "
                        f"{sorted(c2)} on {literal} "
                        f"-> {sorted(resolvent)}"
                    )

                    # Empty clause means contradiction
                    if not resolvent:
                        empty_clause_found = True
                        break

                    # Skip tautologies
                    if any(
                        complement(x) in resolvent
                        for x in resolvent
                    ):
                        continue

                    frozen = frozenset(resolvent)

                    if frozen not in known:
                        new_clauses.add(frozen)

                if empty_clause_found:
                    break

            if empty_clause_found:
                break

        if empty_clause_found:
            break

    if empty_clause_found:
        break

    if not new_clauses:
        break

    known.update(new_clauses)

print("\n--- Final Result ---")

if empty_clause_found:
    print("Empty clause derived: Yes")
    print("Contradiction found.")
    print("Therefore, the goal 'Happy' is proved.")
else:
    print("Empty clause derived: No")
    print("The goal could not be proved.")
