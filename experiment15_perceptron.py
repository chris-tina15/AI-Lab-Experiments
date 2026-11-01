import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = load_breast_cancer()

X = data.data
y = 1 - data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create Perceptron model
model = make_pipeline(
    StandardScaler(),
    Perceptron(
        max_iter=1000,
        eta0=0.1,
        random_state=42
    )
)

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Breast Cancer Classification Using Perceptron")
print("-----------------------------------------------")
print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

print("\nClassification Accuracy: {:.2f}%".format(accuracy * 100))

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Benign", "Malignant"]
))

# Predict a new sample
new_sample = X_test[0].reshape(1, -1)
prediction = model.predict(new_sample)

print(
    "New Sample Prediction:",
    "Malignant" if prediction[0] == 1 else "Benign"
)