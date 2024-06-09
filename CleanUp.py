import pandas as pd

# Load your dataset
df = pd.read_csv('Data/micro_world_139countries.csv')
columns_to_keep = ['economy', 'economycode', 'regionwb', 'pop_adult', 'wpid_random', 'wgt', 'female', 'age', 'educ', 'inc_q', 'emp_in', 'urbanicity_f2f','internetaccess','saved', 'anydigpayment']
df_cleaned = df[columns_to_keep]
# Save the cleaned dataset
df_cleaned.to_csv('Data/Clean_data.csv', index=False)

data_csv_path = 'Data/Clean_data.csv'
data_df = pd.read_csv(data_csv_path)

# Load the second CSV file (contains id, key, text)
mapping_csv_path = 'Data/variable_id_name.csv'
mapping_df = pd.read_csv(mapping_csv_path)

# Create a dictionary from the second CSV file
# Assuming 'key' is the old column name and 'text' is the new column name
# rename_dict = pd.Series(mapping_df.Label.values, index=mapping_df.Name).to_dict()
rename_dict = {row['Name']: f"{row['ColumnName']}" for _, row in mapping_df.iterrows()}

# Rename the columns in the first CSV file using the dictionary
data_df.rename(columns=rename_dict, inplace=True)

# Save the updated first CSV file
updated_csv_path = 'Data/Pre-Processed-Data.csv'
data_df.to_csv(updated_csv_path, index=False)

##############