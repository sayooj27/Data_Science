import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

# Read the dataset
data = pd.read_csv('Iris.csv')

# Display first 5 rows
print(data.head())

# Independent variable (X)
x = data['PetalWidthCm']
print("\nX values:")
print(x.head())

# Dependent variable (Y)
y = data['PetalLengthCm']
print("\nY values:")
print(y.head())

# Convert to NumPy array and reshape
x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)

print("\nX:")
print(x)

print("\nY:")
print(y)

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=42
)

# Create Linear Regression model
classifier = LinearRegression()

# Train the model
classifier.fit(x_train, y_train)

# Predict test values
y_pred = classifier.predict(x_test)

print("\nPredicted values:")
print(y_pred)

# Evaluation
print("\nR-squared score:", r2_score(y_test, y_pred))
print("Mean squared error:", mean_squared_error(y_test, y_pred))

# Coefficient
print("Coefficient:", classifier.coef_)
print("Intercept:", classifier.intercept_)

# Plot actual values
plt.scatter(x_test, y_test, color='blue', label='Actual')

# Plot predicted regression line
plt.plot(x_test, y_pred, color='black', label='Predicted')

plt.xlabel('Petal Width (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Linear Regression Result')
plt.legend()

# Save graph
plt.savefig("prgrm32.png")

# Display graph
plt.show()
