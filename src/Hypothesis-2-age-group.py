import pandas as pd
from scipy.stats import chi2_contingency

# Load the data
df = pd.read_csv('Data/Pre-Processed-Data.csv')

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
df['Age_Group'] = df['Age'].apply(create_age_groups)

# Create a contingency table for Age_Group and Digital Payment usage
contingency_table = pd.crosstab(df['Age_Group'], df['Made_or_received_a_digital_payment'])

# Perform the chi-squared test
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Print the contingency table
print("Contingency Table:")
print(contingency_table)
print(chi2_contingency(contingency_table))

# Print the results of the chi-squared test
print("\nChi-squared Test Results:")
print(f"Chi-squared Statistic: {chi2}")
print(f"P-value: {p_value}")

# Interpretation of the result
if p_value < 0.05:
    print("Result: Reject the null hypothesis - Age group has a significant effect on the usage of digital payments.")
else:
    print("Result: Do not reject the null hypothesis - There is no significant effect of age group on the usage of digital payments.")
