import numpy as np

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Load Wine dataset
wine = load_wine()

X = wine.data
y = wine.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create Gaussian Naive Bayes model
model = GaussianNB()

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Wine Classification Using Naive Bayes")
print("--------------------------------------")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

print("\nClassification Accuracy: {:.2f}%".format(
    accuracy * 100
))

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=wine.target_names
))

# Predict a new sample
new_sample = X_test[0].reshape(1, -1)
prediction = model.predict(new_sample)

print(
    "New Sample Prediction:",
    wine.target_names[prediction[0]]
)