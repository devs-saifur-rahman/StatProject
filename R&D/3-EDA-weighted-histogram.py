import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
import numpy as np

# Create the results directory if it does not exist
os.makedirs('results', exist_ok=True)

# Load the list of independent variables from the text file
independent_vars_file = 'Data/Indp_Variables.csv'
with open(independent_vars_file, 'r', encoding='utf-8-sig') as file:
    independent_vars = file.read().strip().split(',')

# Load the encoded dataset
encoded_data = pd.read_csv('Data/encoded_dataset.csv')

# Define the dependent variable
dependent_var = 'Made_Or_Received_A_Digital_Payment'

# Ensure the dataset includes only the necessary columns
# encoded_data = encoded_data[independent_vars + [dependent_var, 'Weight']]


# Function to calculate weighted mean
def weighted_mean(data, values, weights):
    return (data[values] * data[weights]).sum() / data[weights].sum()


# List of numerical variables to analyze
numerical_vars = ['Age']

# Calculate and print weighted means for numerical variables
weighted_means = {var: weighted_mean(encoded_data, var, 'Weight') for var in numerical_vars}
print("Weighted Means:", weighted_means)

# Save weighted means to a text file
with open('results/weighted_means.txt', 'w') as f:
    for var, mean in weighted_means.items():
        f.write(f'{var}: {mean}\n')


# Function to create and save weighted histograms
def weighted_histogram(data, column, weights, bins=30, save_path='results'):
    plt.figure()
    plt.hist(data[column], bins=bins, weights=data[weights], edgecolor='black')
    plt.title(f'Weighted Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Weighted Frequency')
    plt.savefig(f'{save_path}/weighted_histogram_{column}.png')
    plt.close()


# Function to create and save weighted boxplots by replicating data points
def weighted_boxplot(data, column, weights, save_path='results'):
    plt.figure()
    expanded_data = np.repeat(data[column].values, weights)
    sns.boxplot(x=expanded_data)
    plt.title(f'Weighted Boxplot of {column}')
    plt.xlabel(column)
    plt.savefig(f'{save_path}/weighted_boxplot_{column}.png')
    plt.close()


# Function to calculate detailed statistics and save to a text file
def calculate_statistics(data, column, weights, save_path='results'):
    expanded_data = np.repeat(data[column].values, weights)
    q1 = np.percentile(expanded_data, 25)
    median = np.percentile(expanded_data, 50)
    q3 = np.percentile(expanded_data, 75)
    iqr = q3 - q1
    lower_whisker = max(min(expanded_data), q1 - 1.5 * iqr)
    upper_whisker = min(max(expanded_data), q3 + 1.5 * iqr)
    n = len(expanded_data)
    outliers = expanded_data[(expanded_data < lower_whisker) | (expanded_data > upper_whisker)]

    stats = {
        'Q1': q1,
        'Median': median,
        'Q3': q3,
        'IQR': iqr,
        'Lower Whisker': lower_whisker,
        'Upper Whisker': upper_whisker,
        'N': n,
        'Outliers': outliers.tolist()
    }

    with open(f'{save_path}/statistics_{column}.txt', 'w') as f:
        for key, value in stats.items():
            f.write(f'{key}: {value}\n')


# Create and save weighted histograms, boxplots, and detailed statistics for numerical variables
for var in numerical_vars:
    weighted_histogram(encoded_data, var, 'Weight')
    weighted_boxplot(encoded_data, var, encoded_data['Weight'].astype(int))
    calculate_statistics(encoded_data, var, encoded_data['Weight'].astype(int))

# Analyzing the distribution of categorical variables
categorical_vars = [col for col in independent_vars if col not in numerical_vars]

categorical_distribution = {}

for var in categorical_vars:
    counts = encoded_data[var].value_counts(normalize=True) * 100
    categorical_distribution[var] = counts.to_dict()

# Save categorical distribution to a JSON file
with open('results/categorical_distribution.json', 'w') as f:
    json.dump(categorical_distribution, f, indent=4)


# Function to create and save bar plots for categorical variables
def bar_plot(data, column, save_path='results'):
    plt.figure()
    counts = data[column].value_counts(normalize=True) * 100
    counts.plot(kind='bar', edgecolor='black')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Percentage')
    plt.savefig(f'{save_path}/bar_plot_{column}.png')
    plt.close()


# Create and save bar plots for categorical variables
for var in categorical_vars:
    bar_plot(encoded_data, var)

print("EDA completed and results saved in the 'results' folder.")
