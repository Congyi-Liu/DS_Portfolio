import pandas as pd
import matplotlib.pyplot as plt

# Scrape data from the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
tables = pd.read_html(url, match='Country/Territory')

# Select the table of interest
df = tables[0]

# Flatten multi-level column headers
df.columns = ['_'.join(col).strip() for col in df.columns.values]

# Rename columns to desired format
df = df.rename(columns={'Country/Territory_Country/Territory': 'Country', 
                        'IMF[1][13]_Forecast': 'GDP_USD', 
                        'IMF[1][13]_Year': 'Year'})

# Clean up the data
df['Country'] = df['Country'].str.replace(r'\[.*\]', '', regex=True)
df['GDP_USD'] = df['GDP_USD'].replace('—', None)  # Replace '—' with NaN
df['GDP_USD'] = df['GDP_USD'].str.replace(',', '').astype(float)
df.dropna(subset=['Country', 'GDP_USD'], inplace=True)

# Save to a tidy format (CSV)
df.to_csv('gdp_data_tidy.csv', index=False)

# Plotting the top 10 countries by GDP
top10 = df.sort_values(by='GDP_USD', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top10['Country'], top10['GDP_USD'], color='skyblue')
plt.xlabel('GDP in USD')
plt.title('Top 10 Countries by GDP')
plt.gca().invert_yaxis()
plt.show()
