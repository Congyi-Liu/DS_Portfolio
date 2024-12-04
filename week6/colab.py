import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
series_dataset_ids = {
    'L55O': 'MM23',  # CPIH
    'MGRZ': 'MM23',  # RPI
    'ABMI': 'UKEA',  # GDP
    'BKTL': 'LMS',   # Unemployment Rate
    'D7BT': 'LMS',   # Employment Rate
    'KLS2': 'LMS',   # Average Weekly Earnings
    'MGRQ': 'MM23',  # PPI
    'CHAW': 'LMS',   # Economic Inactivity Rate
    'IHYM': 'LMS'    # Claimant Count
}
base_url = 'https://api.ons.gov.uk/timeseries/{}/dataset/{}/data'

for series_id, dataset_id in series_dataset_ids.items():
    url = base_url.format(series_id, dataset_id)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(f'{series_id}.json', 'w') as f:
            json.dump(data, f)
        print(f'Successfully saved {series_id}.json')
    else:
        print(f'Failed to retrieve data for series {series_id}')
def plot_time_series(series_id, title):
    with open(f'{series_id}.json', 'r') as f:
        data = json.load(f)
    
    # Extract dates and values
    dates = [entry['date'] for entry in data['months']]
    values = [float(entry['value']) for entry in data['months']]
    
    # Create DataFrame
    df = pd.DataFrame({'Date': pd.to_datetime(dates), 'Value': values})
    df.set_index('Date', inplace=True)
    
    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Value'], marker='o')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

# Example usage
plot_time_series('L55O', 'Consumer Prices Index including owner occupiers\' housing costs (CPIH)')
