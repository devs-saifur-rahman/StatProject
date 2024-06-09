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
result_dir = 'Result/Logistic'
os.makedirs(result_dir, exist_ok=True)

# Load the dataset
csv_file_path = 'Data/Pre-Processed-Data.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(csv_file_path)

# Encode categorical variables
label_encoders = {}
categorical_vars = ['Internet_access', 'Income_Quality', 'Region', 'Country', 'Residence','Education','Gender','Saved_in_the_past_year']

for var in categorical_vars:
    le = LabelEncoder()
    data[var] = le.fit_transform(data[var].astype(str))
    label_encoders[var] = le

# Map "Made_or_received_a_digital_payment" to 0 and 1 if necessary
# data['Made_or_received_a_digital_payment'] = data['Made_or_received_a_digital_payment'].map({'No': 0, 'Yes': 1})

# Define the dependent variable
dependent_var = 'Made_or_received_a_digital_payment'

def logistic_regression_analysis(independent_var):

    os.makedirs(result_dir+f'/{independent_var}', exist_ok=True)
    # Prepare the X (independent variable) and y (dependent variable)
    X = data[[independent_var]]
    y = data[dependent_var]

    # Add a constant to the model (intercept)
    X = sm.add_constant(X)

    # Fit the logistic regression model
    logit_model = sm.Logit(y, X).fit()

    # Save logistic regression summary
    summary_file_path = os.path.join(result_dir+f'/{independent_var}', f'Logistic_Regression_Summary_{independent_var}.txt')
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
    plt.title(f'Confusion Matrix for {independent_var} Prediction')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    confusion_matrix_path = os.path.join(result_dir+f'/{independent_var}', f'Confusion_Matrix_{independent_var}.png')
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
    plt.title(f'Receiver Operating Characteristic (ROC) Curve for {independent_var}')
    plt.legend(loc="lower right")
    roc_curve_path = os.path.join(result_dir+f'/{independent_var}', f'ROC_Curve_{independent_var}.png')
    plt.savefig(roc_curve_path)
    plt.close()

    # Sigmoid Curve for Independent Variable
    unique_values = np.sort(data[independent_var].unique())
    X_test = pd.DataFrame({independent_var: unique_values})
    X_test = sm.add_constant(X_test)
    y_test_pred_prob = logit_model.predict(X_test)

    plt.figure(figsize=(10, 7))
    plt.plot(unique_values, y_test_pred_prob, color='red', linewidth=3)
    plt.scatter(data[independent_var], y, color='black', zorder=20, alpha=0.5)
    plt.xlabel(independent_var)
    plt.ylabel('Probability of Digital Payment')
    plt.title(f'Logistic Regression Sigmoid Curve for {independent_var}')
    sigmoid_curve_path = os.path.join(result_dir+f'/{independent_var}', f'Sigmoid_Curve_{independent_var}.png')
    plt.savefig(sigmoid_curve_path)
    plt.close()

    # Correlation Analysis
    correlation = data[[independent_var, dependent_var]].corr()
    correlation_matrix_path = os.path.join(result_dir+f'/{independent_var}', f'Correlation_Matrix_{independent_var}.txt')
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

    json_file_path = os.path.join(result_dir+f'/{independent_var}', f'Results_{independent_var}.json')
    with open(json_file_path, 'w') as json_file:
        json.dump(results, json_file, indent=4)

# Variables to analyze
variables_to_analyze = ['Internet_access', 'Income_Quality', 'Region', 'Country', 'Residence','Education','Gender','Saved_in_the_past_year']

# Perform logistic regression and correlation analysis for each variable
for independent_var in variables_to_analyze:
    logistic_regression_analysis(independent_var)

print("Analysis complete. Results have been saved in the 'Result/Logistic' directory.")
