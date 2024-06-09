import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
csv_file_path = 'Data/Pre-Processed-Data.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(csv_file_path)

# Display the first few rows and columns to understand its structure
# print("First few rows of the dataset:")
# print(data.head())
# print("\nColumns in the dataset:")
# print(data.columns.tolist())

# Replace the values in "Made_or_received_a_digital_payment" with 0 and 1
# data['Made_or_received_a_digital_payment'] = data['Made_or_received_a_digital_payment'].map({'No': 0, 'Yes': 1})

# Define the configurations for histograms
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

# Generate histograms for each configuration
for x_col, hue_col in configurations:
    plt.figure(figsize=(10, 7))
    sns.histplot(data=data, x=x_col, hue=hue_col, multiple="stack", shrink=0.8)

    # Set titles and labels
    plt.title(f'Histogram of {hue_col} by {x_col}')
    plt.xlabel(x_col)
    plt.ylabel('Count')
    plt.legend(title=hue_col, labels=['No', 'Yes'])

    # Display the plot
    plt.xticks(rotation=90)
    plt.show()
