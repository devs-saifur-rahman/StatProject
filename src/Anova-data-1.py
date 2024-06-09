import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load the CSV file
file_path = 'Data/Pre-Processed-Data.csv'
data = pd.read_csv(file_path)

# Rename columns to avoid spaces and special characters issues
data.rename(columns={'Saved_in_the_past_year': 'Saved'}, inplace=True)

# Perform ANOVA with multiple independent variables
model = ols('Made_or_received_a_digital_payment ~ Age + C(Gender) + Income_Quality + Internet_access + Education + C(Residence) + Saved', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Calculate Mean Sum of Squares
anova_table['mean_sq'] = anova_table['sum_sq'] / anova_table['df']

# Display the ANOVA table

print(anova_table)
