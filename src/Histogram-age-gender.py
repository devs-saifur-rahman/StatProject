import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the Result directory if it doesn't exist
os.makedirs('Result', exist_ok=True)

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
    elif age < 90:
        return '80-89'
    else:
        return '90-99'

# Apply age grouping
data['Age_Group'] = data['Age'].apply(create_age_groups)

# Function to plot grouped histograms
def plot_grouped_histogram(data, x, y, group_by):
    plt.figure(figsize=(12, 8))
    sns.histplot(
        data=data,
        x=x,
        hue=group_by,
        multiple="dodge",
        shrink=0.8,
        stat="count",
        palette="viridis"
    )
    plt.xlabel(f'{x.replace("_", " ")}')
    plt.ylabel('Count')
    plt.title(f'Grouped Histogram of {y.replace("_", " ")} by {x.replace("_", " ")} and {group_by.replace("_", " ")}')
    plt.legend(title=group_by.replace("_", " "), labels=['Female', 'Male'])
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'Result/Histogram/{x}_{y}_{group_by}_grouped_histogram.png')
    plt.close()

# Configuration
x = "Age_Group"
y = "Made_or_received_a_digital_payment"
group_by = "Gender"

# Plot grouped histogram
plot_grouped_histogram(data, x, y, group_by)
