import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# Load breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target.reshape(-1, 1)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Standardize data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Neural network architecture
input_neurons = X_train.shape[1]
hidden_neurons = 8
output_neurons = 1

np.random.seed(42)

W1 = np.random.randn(input_neurons, hidden_neurons) * np.sqrt(2 / input_neurons)
b1 = np.zeros((1, hidden_neurons))

W2 = np.random.randn(hidden_neurons, output_neurons) * np.sqrt(2 / hidden_neurons)
b2 = np.zeros((1, output_neurons))

# Sigmoid activation function
def sigmoid(x):
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))

# Training parameters
learning_rate = 0.05
epochs = 3000

# Training using forward and backward propagation
for epoch in range(epochs):

    # Forward propagation
    hidden_input = np.dot(X_train, W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    predicted_output = sigmoid(final_input)

    # Backpropagation
    output_delta = (predicted_output - y_train) / len(y_train)

    dW2 = np.dot(hidden_output.T, output_delta)
    db2 = np.sum(output_delta, axis=0, keepdims=True)

    hidden_delta = (
        np.dot(output_delta, W2.T)
        * hidden_output * (1 - hidden_output)
    )

    dW1 = np.dot(X_train.T, hidden_delta)
    db1 = np.sum(hidden_delta, axis=0, keepdims=True)

    # Update weights and biases
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

# Test the network
hidden_test = sigmoid(np.dot(X_test, W1) + b1)
test_output = sigmoid(np.dot(hidden_test, W2) + b2)

y_pred = (test_output >= 0.5).astype(int)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Artificial Neural Network using Backpropagation")
print("-----------------------------------------------")
print("Input neurons:", input_neurons)
print("Hidden neurons:", hidden_neurons)
print("Output neurons:", output_neurons)
print("Training epochs:", epochs)

print("\nClassification Accuracy:", round(accuracy * 100, 2), "%")

print("\nConfusion Matrix:")
print(cm)

print("\nClass Labels:")
print("0 - Malignant")
print("1 - Benign")