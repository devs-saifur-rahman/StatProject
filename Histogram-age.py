import os
import pandas as pd
import matplotlib.pyplot as plt

# Create the Result directory if it doesn't exist
os.makedirs('Result/Histogram', exist_ok=True)

# Load the dataset
data = pd.read_csv('Data/Pre-Processed-Data.csv')

# Function to create age groups
def create_age_groups(age):
    if age < 10:
        return '0-9'
    elif age < 20:
        return '10-19'
    elif age < 30:
        return '20-29'
    elif age < 40:
        return '30-39'
    elif age < 50:
        return '40-49'
    elif age < 60:
        return '50-59'
    elif age < 70:
        return '60-69'
    elif age < 80:
        return '70-79'
    else:
        return '80+'

# Apply age grouping
data['Age_Group'] = data['Age'].apply(create_age_groups)

# Function to plot histograms
def plot_histogram(data, x, y):
    plt.figure(figsize=(12, 8))
    data.groupby(x)[y].value_counts(normalize=True).unstack().plot(kind='bar', stacked=True, color=['blue', 'orange'])
    plt.xlabel(x.replace('_', ' '))
    plt.ylabel('Proportion')
    plt.title(f'Proportion of {y.replace("_", " ")} by {x.replace("_", " ")}')
    plt.legend(['No', 'Yes'])
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'Result/Histogram/{x}_{y}_histogram.png')
    plt.close()

# Configuration for Age_Group
x = "Age_Group"
y = "Made_or_received_a_digital_payment"

# Plot histogram
plot_histogram(data, x, y)
