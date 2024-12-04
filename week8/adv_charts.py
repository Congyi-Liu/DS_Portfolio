import matplotlib.pyplot as plt

# Data (dummy example, replace with your own dataset)
countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan']
gdp = [13.6, 2.7, 21.4, 1.1, 0.3]  # Trillions of USD
population = [1440, 1390, 331, 273, 225]  # Millions
co2_emissions = [10.065, 2.654, 4.766, 0.588, 0.2]  # Billions of metric tons

# Create bubble chart
plt.figure(figsize=(10, 6))
bubble_sizes = [p / 2 for p in population]  # Scale the bubbles based on population size

plt.scatter(gdp, co2_emissions, s=bubble_sizes, alpha=0.5, c=range(len(countries)), cmap='viridis', edgecolors="w", linewidth=1)

for i, country in enumerate(countries):
    plt.text(gdp[i], co2_emissions[i], country, fontsize=10, ha='right')

plt.xlabel('GDP (Trillions USD)')
plt.ylabel('CO2 Emissions (Billions of Metric Tons)')
plt.title('Relationship between GDP, Population Size, and CO2 Emissions')
plt.grid(True)
plt.colorbar(label='Country Index')
plt.show()

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generating random data for stock returns (dummy example, replace with your own dataset)
np.random.seed(42)
data = {
    'Stock_A': np.random.randn(100),
    'Stock_B': np.random.randn(100),
    'Stock_C': np.random.randn(100),
    'Stock_D': np.random.randn(100),
    'Stock_E': np.random.randn(100),
}

stock_returns = pd.DataFrame(data)

# Calculate correlation matrix
correlation_matrix = stock_returns.corr()

# Create heat map
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)

plt.title('Correlation Between Stock Returns')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generating random income data (dummy example, replace with your dataset)
np.random.seed(42)
income = np.random.lognormal(mean=10, sigma=0.8, size=1000)

# Create the histogram
plt.figure(figsize=(10, 6))
plt.hist(income, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Add labels and title
plt.xlabel('Income (in USD)')
plt.ylabel('Frequency')
plt.title('Income Distribution Histogram')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()
