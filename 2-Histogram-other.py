import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
csv_file_path = 'F:/mba/511.3/Project/PythonProject/Final/Pre-Processed-Data.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(csv_file_path)

# Display the first few rows and columns to understand its structure
# print("First few rows of the dataset:")
# print(data.head())
# print("\nColumns in the dataset:")
# print(data.columns.tolist())

# Replace the values in "Made or received a digital payment" with 0 and 1
# data['Made or received a digital payment'] = data['Made or received a digital payment'].map({'No': 0, 'Yes': 1})

# Define the configurations for histograms
configurations = [
    ("Region", "Made or received a digital payment"),
    ("Country", "Made or received a digital payment"),
    ("Education", "Made or received a digital payment"),
    ("Internet access", "Made or received a digital payment"),
    ("Income Quality", "Made or received a digital payment"),
    ("Residence", "Made or received a digital payment"),
    ("Gender", "Made or received a digital payment"),
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
