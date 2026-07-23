import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Feature names
feature_names = iris.feature_names

# Scatter plot: Sepal Length vs Sepal Width
plt.figure()
for i in range(3):
    plt.scatter(
        X[y == i, 0],  # Sepal Length
        X[y == i, 1],  # Sepal Width
        label=iris.target_names[i]
    )

plt.xlabel(feature_names[0])
plt.ylabel(feature_names[1])
plt.title("Iris Dataset - Sepal Length vs Width")
plt.legend()
plt.show()