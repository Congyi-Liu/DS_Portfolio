# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Generate a sample dataset for the task
np.random.seed(42)
data = pd.DataFrame({
    'feature1': np.random.rand(100) * 100,
    'feature2': np.random.rand(100) * 200,
    'target': np.random.rand(100) * 50
})

# ------------------------------
# Task 1: Supervised Learning (Regression)
# ------------------------------

# Prepare the data
X = data[['feature1', 'feature2']]  # Features
y = data['target']                 # Target

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Apply Linear Regression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Make predictions
y_pred = regressor.predict(X_test)

# Plot the results
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', label='Perfect Fit')
plt.title('Linear Regression: Actual vs Predicted')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.legend()
plt.tight_layout()
plt.show()

# ------------------------------
# Task 2: Unsupervised Learning (Clustering)
# ------------------------------

# Apply KMeans Clustering
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Plot the clusters
plt.figure(figsize=(8, 6))
plt.scatter(data['feature1'], data['feature2'], c=data['Cluster'], cmap='viridis', alpha=0.7)
plt.title('KMeans Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster')
plt.tight_layout()
plt.show()
