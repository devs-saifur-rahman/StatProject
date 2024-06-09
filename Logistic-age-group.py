import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, roc_curve, auc, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json

# Create directories to save results if they don't exist
result_dir = 'Result/Logistic-Age-Group'
os.makedirs(result_dir, exist_ok=True)

# Load the dataset
csv_file_path = 'Data/Pre-Processed-Data.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(csv_file_path)

# Map "Made_or_received_a_digital_payment" to 0 and 1 if necessary
# data['Made_or_received_a_digital_payment'] = data['Made_or_received_a_digital_payment'].map({'No': 0, 'Yes': 1})

# Group "Age" into 10-year ranges
data['Age Group'] = pd.cut(data['Age'], bins=range(0, 101, 10), right=False, labels=[f'{i}-{i+9}' for i in range(0, 100, 10)])

# Encode the new age group variable
le = LabelEncoder()
data['Age Group'] = le.fit_transform(data['Age Group'].astype(str))

# Define the dependent variable
dependent_var = 'Made_or_received_a_digital_payment'

# Define the independent variable
independent_var = 'Age Group'

# Prepare the X (independent variable) and y (dependent variable)
X = data[[independent_var]]
y = data[dependent_var]

# Add a constant to the model (intercept)
X = sm.add_constant(X)

# Fit the logistic regression model
logit_model = sm.Logit(y, X).fit()

# Save logistic regression summary
summary_file_path = os.path.join(result_dir, 'Logistic_Regression_Summary.txt')
with open(summary_file_path, 'w') as file:
    file.write(logit_model.summary2().as_text())

# Predict the probabilities
y_pred_prob = logit_model.predict(X)

# Classify based on a threshold of 0.5
y_pred = (y_pred_prob >= 0.5).astype(int)

# Confusion Matrix
cm = confusion_matrix(y, y_pred)
classification_rep = classification_report(y, y_pred, output_dict=True, zero_division=0)

# ROC Curve
fpr, tpr, _ = roc_curve(y, y_pred_prob)
roc_auc = auc(fpr, tpr)

# Plot Confusion Matrix
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
plt.title('Confusion Matrix for Digital Payment Prediction')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
confusion_matrix_path = os.path.join(result_dir, 'Confusion_Matrix.png')
plt.savefig(confusion_matrix_path)
plt.close()

# Plot ROC Curve
plt.figure(figsize=(10, 7))
plt.plot(fpr, tpr, color='blue', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='red', lw=2, linestyle='--', label='Random Guess')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
roc_curve_path = os.path.join(result_dir, 'ROC_Curve.png')
plt.savefig(roc_curve_path)
plt.close()

# Sigmoid Curve for Age Group
age_group_values = np.sort(data[independent_var].unique())
X_test = pd.DataFrame({independent_var: age_group_values})
X_test = sm.add_constant(X_test)
y_test_pred_prob = logit_model.predict(X_test)

plt.figure(figsize=(10, 7))
plt.plot(age_group_values, y_test_pred_prob, color='red', linewidth=3)
plt.scatter(data[independent_var], y, color='black', zorder=20, alpha=0.5)
plt.xlabel('Age Group')
plt.ylabel('Probability of Digital Payment')
plt.title('Logistic Regression Sigmoid Curve for Age Group')
sigmoid_curve_path = os.path.join(result_dir, 'Sigmoid_Curve.png')
plt.savefig(sigmoid_curve_path)
plt.close()

# Correlation Analysis
correlation = data[[independent_var, dependent_var]].corr()
correlation_matrix_path = os.path.join(result_dir, 'Correlation_Matrix.txt')
with open(correlation_matrix_path, 'w') as file:
    file.write(correlation.to_string())

# Save all relevant information in a JSON file
results = {
    'logistic_regression_summary': logit_model.summary2().as_text(),
    'confusion_matrix': cm.tolist(),
    'roc_auc': roc_auc,
    'classification_report': classification_rep,
    'correlation_matrix': correlation.to_dict()
}

json_file_path = os.path.join(result_dir, 'Results.json')
with open(json_file_path, 'w') as json_file:
    json.dump(results, json_file, indent=4)

print("Analysis complete. Results have been saved in the 'Result/Logistic' directory.")
