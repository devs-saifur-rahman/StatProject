import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

# Load the dataset
csv_file_path = 'Data/Pre-Processed-Data.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(csv_file_path)



# Define fields to analyze
fields_to_analyze = ["Education", "Internet_access", "Income_Quality", "Residence", "Age",'Saved_in_the_past_year', "Gender"]

# Function to generate and save boxplots
def generate_boxplot(data, field):
    plt.figure(figsize=(10, 7))
    sns.boxplot(y=data[field])
    plt.title(f'Boxplot of {field}')
    plt.xticks(rotation=90 if field in ["Region", "Country"] else 0)
    plt.savefig(f'Result/Boxplot/boxplot_{field}.png')
    plt.close()

# Generate and save boxplots for each field
for field in fields_to_analyze:
    generate_boxplot(data, field)

# Function to calculate and print IQR details
def calculate_iqr(data, field):
    Q1 = data[field].quantile(0.25)
    Q2 = data[field].median()
    Q3 = data[field].quantile(0.75)
    IQR = Q3 - Q1
    lower_whisker = Q1 - 1.5 * IQR
    upper_whisker = Q3 + 1.5 * IQR
    outliers = data[(data[field] < lower_whisker) | (data[field] > upper_whisker)][field]
    return {
        "Field": field,
        "Q1": Q1,
        "Median": Q2,
        "Q3": Q3,
        "IQR": IQR,
        "Lower Whisker": lower_whisker,
        "Upper Whisker": upper_whisker,
        "Outliers": list(outliers)
    }

# Calculate and print IQR details for each field
iqr_details = []
for field in fields_to_analyze:
    iqr_details.append(calculate_iqr(data, field))

# Save the IQR details to a JSON file
with open('Result/Boxplot/IQR_details.json', 'w') as f:
    json.dump(iqr_details, f, indent=4)

# Print the IQR details for each field
for detail in iqr_details:
    print(json.dumps(detail, indent=4))
