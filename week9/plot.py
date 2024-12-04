import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
db_item_clean_path = 'db_item_clean.csv'
db_region_path = 'db_region.csv'

db_item_clean = pd.read_csv(db_item_clean_path)
db_region = pd.read_csv(db_region_path)

# Plot 1: Top 5 items with the highest number of observations (n_obs) from db_item_clean
top_items = db_item_clean.nlargest(5, 'n_obs')
plt.figure(figsize=(10, 6))
plt.bar(top_items['description'], top_items['n_obs'], color='skyblue')
plt.title('Top 5 Items by Number of Observations')
plt.xlabel('Item Description')
plt.ylabel('Number of Observations')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot 2: Regional mean prices (p_mean) from db_region
plt.figure(figsize=(10, 6))
plt.bar(db_region['region'], db_region['p_mean'], color='lightgreen')
plt.title('Mean Prices by Region')
plt.xlabel('Region')
plt.ylabel('Mean Price (£)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot 3: Distribution of standard deviation of prices (p_sd) across regions
plt.figure(figsize=(10, 6))
plt.bar(db_region['region'], db_region['p_sd'], color='orange')
plt.title('Standard Deviation of Prices by Region')
plt.xlabel('Region')
plt.ylabel('Price Standard Deviation (£)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
