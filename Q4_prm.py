
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data: Study Hours vs Exam Scores
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
scores = np.array([52, 55, 60, 63, 66, 70, 74, 78, 82])

# Correlation coefficient
correlation = np.corrcoef(hours.flatten(), scores)[0, 1]
print("Correlation Coefficient:", correlation)

# Linear Regression
model = LinearRegression()
model.fit(hours, scores)

a = model.intercept_   # Intercept
b = model.coef_[0]     # Slope

print("Intercept (a):", a)
print("Slope (b):", b)
print(f"Regression Line: y = {a:.2f} + {b:.2f}x")
