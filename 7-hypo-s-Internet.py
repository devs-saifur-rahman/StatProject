import pandas as pd
from scipy.stats import chi2_contingency

# Load the data
df = pd.read_csv('Pre-Processed-Data.csv')

# Create a contingency table for Internet access and Digital Payment usage
contingency_table = pd.crosstab(df['Internet access'], df['Made or received a digital payment'])

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
    print("Result: Reject the null hypothesis - Internet access has a significant effect on the usage of digital payments.")
else:
    print("Result: Do not reject the null hypothesis - There is no significant effect of internet access on the usage of digital payments.")
###


# Create a contingency table for Region and Digital Payment usage
contingency_table = pd.crosstab(df['Region'], df['Made or received a digital payment'])

# Perform the chi-squared test
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Print the contingency table
print("Contingency Table:")
print(contingency_table)

# Print the results of the chi-squared test
print("\nChi-squared Test Results:")
print(f"Chi-squared Statistic: {chi2}")
print(f"P-value: {p_value}")

# Interpretation of the result
if p_value < 0.05:
    print("Result: Reject the null hypothesis - There is a significant effect of region on the usage of digital payments.")
else:
    print("Result: Do not reject the null hypothesis - There is no significant effect of region on the usage of digital payments.")


# Create a contingency table for Country and Digital Payment usage
contingency_table = pd.crosstab(df['Country'], df['Made or received a digital payment'])

# Perform the chi-squared test
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Print the contingency table
print("Contingency Table:")
print(contingency_table)

# Print the results of the chi-squared test
print("\nChi-squared Test Results:")
print(f"Chi-squared Statistic: {chi2}")
print(f"P-value: {p_value}")

# Interpretation of the result
if p_value < 0.05:
    print("Result: Reject the null hypothesis - There is a significant effect of country on the usage of digital payments.")
else:
    print("Result: Do not reject the null hypothesis - There is no significant effect of country on the usage of digital payments.")




# Create a contingency table for Gender and Digital Payment usage
contingency_table = pd.crosstab(df['Gender'], df['Made or received a digital payment'])

# Perform the chi-squared test
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Print the contingency table
print("Contingency Table:")
print(contingency_table)

# Print the results of the chi-squared test
print("\nChi-squared Test Results:")
print(f"Chi-squared Statistic: {chi2}")
print(f"P-value: {p_value}")

# Interpretation of the result
if p_value < 0.05:
    print("Result: Reject the null hypothesis - There is a significant effect of gender on the usage of digital payments.")
else:
    print("Result: Do not reject the null hypothesis - There is no significant effect of gender on the usage of digital payments.")



# Create a contingency table for Education and Digital Payment usage
contingency_table = pd.crosstab(df['Education'], df['Made or received a digital payment'])

# Perform the chi-squared test
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Print the contingency table
print("Contingency Table:")
print(contingency_table)

# Print the results of the chi-squared test
print("\nChi-squared Test Results:")
print(f"Chi-squared Statistic: {chi2}")
print(f"P-value: {p_value}")

# Interpretation of the result
if p_value < 0.05:
    print("Result: Reject the null hypothesis - There is a significant effect of education on the usage of digital payments.")
else:
    print("Result: Do not reject the null hypothesis - There is no significant effect of education on the usage of digital payments.")



# Create a contingency table for Residence and Digital Payment usage
contingency_table = pd.crosstab(df['Residence'], df['Made or received a digital payment'])

# Perform the chi-squared test
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Print the contingency table
print("Contingency Table:")
print(contingency_table)

# Print the results of the chi-squared test
print("\nChi-squared Test Results:")
print(f"Chi-squared Statistic: {chi2}")
print(f"P-value: {p_value}")

# Interpretation of the result
if p_value < 0.05:
    print("Result: Reject the null hypothesis - There is a significant effect of residence type on the usage of digital payments.")
else:
    print("Result: Do not reject the null hypothesis - There is no significant effect of residence type on the usage of digital payments.")
