
import math
import collections

# Customer loan dataset
data = [
    ["Good", "High", "Salaried", "No", "Approved"],
    ["Good", "High", "Self-employed", "No", "Approved"],
    ["Good", "Medium", "Salaried", "No", "Approved"],
    ["Good", "Low", "Salaried", "No", "Approved"],
    ["Good", "Medium", "Self-employed", "Yes", "Approved"],
    ["Good", "Low", "Self-employed", "No", "Approved"],
    ["Poor", "High", "Salaried", "No", "Approved"],
    ["Poor", "Medium", "Salaried", "No", "Approved"],
    ["Poor", "Low", "Salaried", "No", "Rejected"],
    ["Poor", "High", "Self-employed", "Yes", "Rejected"],
    ["Poor", "Medium", "Self-employed", "No", "Rejected"],
    ["Poor", "Low", "Self-employed", "Yes", "Rejected"],
    ["Good", "High", "Salaried", "Yes", "Rejected"],
    ["Good", "Medium", "Self-employed", "Yes", "Rejected"],
    ["Poor", "High", "Salaried", "Yes", "Rejected"],
    ["Poor", "Low", "Salaried", "Yes", "Rejected"]
]

features = [
    "Credit History",
    "Income",
    "Employment",
    "Existing Loan"
]

# Calculate entropy
def calculate_entropy(rows):
    labels = [row[-1] for row in rows]
    counts = collections.Counter(labels)
    total = len(labels)

    entropy = 0

    for count in counts.values():
        probability = count / total
        entropy -= probability * math.log2(probability)

    return entropy


# Calculate information gain
def information_gain(rows, feature_index):
    total_entropy = calculate_entropy(rows)
    groups = collections.defaultdict(list)

    for row in rows:
        groups[row[feature_index]].append(row)

    weighted_entropy = 0

    for group in groups.values():
        weighted_entropy += (
            len(group) / len(rows)
        ) * calculate_entropy(group)

    return total_entropy - weighted_entropy


# Build ID3 decision tree
def build_tree(rows, available_features):
    labels = [row[-1] for row in rows]

    if len(set(labels)) == 1:
        return labels[0]

    if not available_features:
        return collections.Counter(labels).most_common(1)[0][0]

    best_feature = max(
        available_features,
        key=lambda index: information_gain(rows, index)
    )

    tree = {features[best_feature]: {}}

    values = sorted(set(row[best_feature] for row in rows))

    for value in values:
        subset = [
            row for row in rows
            if row[best_feature] == value
        ]

        remaining_features = [
            index for index in available_features
            if index != best_feature
        ]

        tree[features[best_feature]][value] = build_tree(
            subset, remaining_features
        )

    return tree


# Predict loan approval
def predict(tree, sample):
    while isinstance(tree, dict):
        attribute = next(iter(tree))
        value = sample.get(attribute)
        branches = tree[attribute]

        if value not in branches:
            return "Unknown"

        tree = branches[value]

    return tree


# Main program
initial_entropy = calculate_entropy(data)

print("ID3 Decision Tree - Loan Approval")
print("----------------------------------")

print("\nInitial Entropy:", round(initial_entropy, 4))

print("\nInformation Gain:")

for index, feature in enumerate(features):
    gain = information_gain(data, index)
    print(feature, ":", round(gain, 4))

tree = build_tree(data, list(range(len(features))))

print("\nDecision Tree Root:")
print(next(iter(tree)))

samples = [
    {
        "Credit History": "Good",
        "Income": "High",
        "Employment": "Salaried",
        "Existing Loan": "No"
    },
    {
        "Credit History": "Poor",
        "Income": "Low",
        "Employment": "Self-employed",
        "Existing Loan": "Yes"
    },
    {
        "Credit History": "Poor",
        "Income": "High",
        "Employment": "Salaried",
        "Existing Loan": "No"
    }
]

print("\nLoan Application Predictions:")

for i, sample in enumerate(samples, 1):
    result = predict(tree, sample)
    print("Application", i, ":", result)
