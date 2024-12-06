import json
import pandas as pd

# Load datasets
db_item_clean_path = 'db_item_clean.csv'
db_region_path = 'db_region.csv'

db_item_clean = pd.read_csv(db_item_clean_path)
db_region = pd.read_csv(db_region_path)

# Pre-calculated data from the previous Python code
# Top 5 items by number of observations
top_items = db_item_clean.nlargest(5, 'n_obs')
top_items_data = top_items[['description', 'n_obs']].to_dict(orient='records')

# Regional mean prices
mean_prices_data = db_region[['region', 'p_mean']].to_dict(orient='records')

# Regional price standard deviations
price_sd_data = db_region[['region', 'p_sd']].to_dict(orient='records')

# Plot JSONs
plots = {
    "top_items_plot": {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "width": 400,
        "height": 600,
        "data": {
            "values": top_items_data
        },
        "mark": "bar",
        "encoding": {
            "x": {
                "field": "description",
                "type": "nominal",
                "axis": {
                    "labelAngle": 45,
                    "labelAlign": "right"
                }
            },
            "y": {
                "field": "n_obs",
                "type": "quantitative",
                "title": "Number of Observations"
            },
            "color": {
                "value": "#87ceeb"
            }
        },
        "title": "Top 5 Items by Number of Observations"
    },

    "mean_prices_plot": {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "width": 400,
        "height": 600,
        "data": {
            "values": mean_prices_data
        },
        "mark": "bar",
        "encoding": {
            "x": {
                "field": "region",
                "type": "nominal",
                "axis": {
                    "labelAngle": 45,
                    "labelAlign": "right"
                }
            },
            "y": {
                "field": "p_mean",
                "type": "quantitative",
                "title": "Mean Price (£)"
            },
            "color": {
                "value": "#90ee90"
            }
        },
        "title": "Mean Prices by Region"
    },

    "price_sd_plot": {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "width": 400,
        "height": 600,
        "data": {
            "values": price_sd_data
        },
        "mark": "bar",
        "encoding": {
            "x": {
                "field": "region",
                "type": "nominal",
                "axis": {
                    "labelAngle": 45,
                    "labelAlign": "right"
                }
            },
            "y": {
                "field": "p_sd",
                "type": "quantitative",
                "title": "Price Standard Deviation (£)"
            },
            "color": {
                "value": "#ffa500"
            }
        },
        "title": "Standard Deviation of Prices by Region"
    }
}

# Save each plot as a separate JSON file
for plot_name, plot_content in plots.items():
    with open(f"{plot_name}.json", "w") as json_file:
        json.dump(plot_content, json_file, indent=2)
