import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create the Result directory if it doesn't exist
os.makedirs('Result/Histogram', exist_ok=True)

# Load the dataset
data = pd.read_csv('Data/Pre-Processed-Data.csv')

# Function to plot histograms
def plot_histogram(data, x, y, bins=10):
    plt.figure(figsize=(12, 8))
    data.groupby(x)[y].value_counts(normalize=True).unstack().plot(kind='bar', stacked=True, color=['blue', 'orange'])
    plt.xlabel(x)
    plt.ylabel('Proportion')
    plt.title(f'Proportion of {y.replace("_", " ")} by {x.replace("_", " ")}')
    plt.legend(['No', 'Yes'])
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'Result/Histogram/{x}_{y}_histogram.png')
    plt.close()

# Configurations
configurations = [
    ("Region", "Made_or_received_a_digital_payment"),
    ("Country", "Made_or_received_a_digital_payment"),
    ("Education", "Made_or_received_a_digital_payment"),
    ("Internet_access", "Made_or_received_a_digital_payment"),
    ("Income_Quality", "Made_or_received_a_digital_payment"),
    ("Residence", "Made_or_received_a_digital_payment"),
    ("Saved_in_the_past_year", "Made_or_received_a_digital_payment"),
    ("Gender", "Made_or_received_a_digital_payment"),
]

# For the "Country" variable, select 20 countries randomly but ensure even distribution
countries = data['Country'].unique()
np.random.seed(0)  # For reproducibility
selected_countries = np.random.choice(countries, 20, replace=False)
data_filtered = data[data['Country'].isin(selected_countries)]

# Plot histograms
for x, y in configurations:
    if x == "Country":
        plot_histogram(data_filtered, x, y)
    else:
        plot_histogram(data, x, y)
