import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load the CSV file
file_path = 'Pre-Processed-Data.csv'
data = pd.read_csv(file_path)

# Rename columns to avoid spaces and special characters issues
data.rename(columns={'Income Quality': 'Income_Quality','Internet access':'Internat_Access',
                     'Made or received a digital payment': 'Digital_Payment'}, inplace=True)

# Perform ANOVA with multiple independent variables
model = ols('Digital_Payment ~ Age + C(Gender) + Income_Quality + Internat_Access + Education + C(Residence)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Calculate Mean Sum of Squares
anova_table['mean_sq'] = anova_table['sum_sq'] / anova_table['df']

# Display the ANOVA table

print(anova_table)
