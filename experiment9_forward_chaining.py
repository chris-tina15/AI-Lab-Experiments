
# Experiment 9: Forward Chaining

# Initial facts
facts = {
    "fever",
    "cough",
    "high_temperature",
    "age_over_65"
}

# Inference rules
rules = [
    (["fever", "cough"], "respiratory_symptoms"),

    (["respiratory_symptoms", "high_temperature"],
     "suspected_infection"),

    (["suspected_infection", "age_over_65"],
     "priority_consultation")
]

trace = []

print("Forward Chaining Using Facts and Rules\n")

print("Initial Facts:")
for fact in sorted(facts):
    print("-", fact)

# Apply rules until no new facts can be inferred
changed = True

while changed:
    changed = False

    for conditions, conclusion in rules:

        if all(condition in facts for condition in conditions):

            if conclusion not in facts:
                facts.add(conclusion)
                changed = True

                trace.append(
                    f"IF {conditions} THEN {conclusion}"
                )

                print(f"\nRule applied: {trace[-1]}")
                print(f"New fact inferred: {conclusion}")

# Display final facts
print("\n--- Final Facts ---")

for fact in sorted(facts):
    print("-", fact)

print("\n--- Final Conclusion ---")

if "priority_consultation" in facts:
    print("Patient qualifies for a priority consultation.")
else:
    print("Priority consultation criteria not established.")

print("\nTotal new facts inferred:", len(trace))
