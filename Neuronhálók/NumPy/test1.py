import numpy as np
import matplotlib.pyplot as plt

#Linear regression

# Generate some random data (y = 3x + 2 with some noise)
np.random.seed(42)
X = np.linspace(0, 10, 100)  # Features
Y = 3 * X + 2 + np.random.randn(100) * 2 

# Initialize parameters (slope m and bias b)
m, b = np.random.randn(), np.random.randn()

# Learning rate and iterations
learning_rate = 0.01
epochs = 1000

# Gradient Descent
for _ in range(epochs):
    Y_pred = m * X + b  # Predicted values
    error = Y_pred - Y  # Error

    # Compute gradients
    dm = (2 / len(X)) * np.sum(error * X)
    db = (2 / len(X)) * np.sum(error)

    # Update parametersc 
    m -= learning_rate * dm
    b -= learning_rate * db

# Plot the results
plt.scatter(X, Y, label="Data")
plt.plot(X, m * X + b, color="red", label="Fitted Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

print(f"Final Model: y = {m:.2f}x + {b:.2f}")
