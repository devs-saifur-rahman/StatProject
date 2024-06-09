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

# Group "Respondent age" into 10-year ranges
data['Age Group'] = pd.cut(data['Age'], bins=range(0, 101, 10), right=False, labels=[f'{i}-{i+9}' for i in range(0, 100, 10)])

# Calculate the percentage of "yes" and "no" in "Made or received a digital payment" for each age group
age_group_percentages = data.groupby('Age Group')['Made or received a digital payment'].value_counts(normalize=True).unstack().fillna(0) * 100

# Plot the percentages
plt.figure(figsize=(12, 8))
age_group_percentages.plot(kind='bar', stacked=True)

# Set titles and labels
plt.title('Percentage of Digital Payment by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Percentage')
plt.legend(title='Made or Received a Digital Payment', labels=['No', 'Yes'])

# Display the plot
plt.xticks(rotation=45)
plt.show()
