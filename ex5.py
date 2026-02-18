import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
np.random.seed(0)
X = np.random.rand(100) * 10
Y = 2.5 * X + np.random.normal(0, 2, 100)
plt.scatter(X, Y, color='blue', alpha=0.7)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot: X vs Y')
plt.show()
