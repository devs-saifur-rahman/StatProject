import pandas as pd

# Load your dataset
data = pd.read_csv('Data/ProcessedData.csv')  # Replace 'your_dataset.csv' with your actual file path

# Define the mappings based on the provided information
gender_mapping = {1: 'Female', 2: 'Male'}
education_mapping = {
    1: 'Primary or Less',
    2: 'Secondary',
    3: 'Tertiary or More',
    4: 'Do Not Know',
    5: 'Refused to Answer'
}
income_quality_mapping = {
    1: 'Poorest 20%',
    2: 'Second 20%',
    3: 'Middle 20%',
    4: 'Fourth 20%',
    5: 'Richest 20%'
}
internet_access_mapping = {
    1: 'Yes',
    2: 'No',
    3: 'Do Not Know',
    4: 'Refused to Answer'
}
saved_mapping = {1: 'Yes', 0: 'No'}
residence_mapping = {1: 'Rural', 2: 'Urban'}

# Apply the mappings to the relevant columns
data['Gender'] = data['Gender'].map(gender_mapping)
data['Education'] = data['Education'].map(education_mapping)
data['Income_Quality'] = data['Income_Quality'].map(income_quality_mapping)
data['Internet_Access'] = data['Internet_Access'].map(internet_access_mapping)
data['Saved_In_The_Past_Year'] = data['Saved_In_The_Past_Year'].map(saved_mapping)
data['Residence'] = data['Residence'].map(residence_mapping)

# Include the necessary independent and dependent variables
# We keep 'Age' and 'Made_Or_Received_A_Digital_Payment' in the dataset
# Also ensure 'Weight' is retained for weighted analysis
variables_to_keep = [
    'Age', 'Made_Or_Received_A_Digital_Payment', 'Weight', 'Population_15_up',
    'Gallup_World_Poll_identifier', 'Respondent_Is_In_Workforce', 'Country',
    'Country_Code', 'Region', 'Gender', 'Education', 'Income_Quality',
    'Saved_In_The_Past_Year', 'Internet_Access', 'Residence'
]

data = data[variables_to_keep]

# One-Hot Encoding for categorical variables
encoded_data = pd.get_dummies(data, columns=[
    'Country', 'Country_Code', 'Region', 'Gender', 'Education',
    'Income_Quality', 'Saved_In_The_Past_Year', 'Internet_Access', 'Residence'
], drop_first=True)

# Display the first few rows of the encoded dataset to verify
print(encoded_data.head())

# Save the encoded data to a new CSV file
encoded_data.to_csv('Data/encoded_dataset.csv', index=False)
