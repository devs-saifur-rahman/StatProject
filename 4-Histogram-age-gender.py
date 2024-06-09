import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
csv_file_path = 'F:/mba/511.3/Project/PythonProject/Final/Pre-Processed-Data.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(csv_file_path)


# Display the first few rows and columns to understand its structure
print("First few rows of the dataset:")
print(data.head())
print("\nColumns in the dataset:")
print(data.columns.tolist())

# Replace the values in "Made or received a digital payment" with 0 and 1
# data['Made or received a digital payment'] = data['Made or received a digital payment'].map({'No': 0, 'Yes': 1})

# Group "Respondent age" into 10-year ranges
data['Age Group'] = pd.cut(data['Age'], bins=range(0, 101, 10), right=False, labels=[f'{i}-{i+9}' for i in range(0, 100, 10)])

# Create a combined Age-Gender group
data['Age-Gender Group'] = data['Age Group'].astype(str) + " - " + data['Gender'].astype(str)

# Create a grouped histogram using seaborn
plt.figure(figsize=(15, 10))
sns.histplot(data=data, x='Age Group', hue='Gender', multiple='dodge', shrink=0.8, hue_order=['Male', 'Female'])

# Set titles and labels
plt.title('Grouped Histogram of Digital Payment by Age Group and Gender')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.legend(title='Gender', labels=['Female', 'Male'])

# Display the plot
plt.xticks(rotation=45)
plt.show()

