import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc, confusion_matrix, classification_report
import json
import os


def main():
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)
    data_path = '../Data/Pre-Processed-Data.csv'
    data = pd.read_csv(data_path)
    data.drop(['Country_Code', 'Gallup_World_Poll_identifier', 'Weight', 'Population_15_up'], axis=1, inplace=True)
    data.dropna(inplace=True)

    # Encode categorical variables
    categorical_vars = ['Country', 'Region', 'Gender', 'Education', 'Income_Quality', 'Residence', 'Internet_access',
                        'Saved_in_the_past_year']
    for var in categorical_vars:
        data[var] = LabelEncoder().fit_transform(data[var].astype(str))

    X = data.drop('Made_or_received_a_digital_payment', axis=1)
    y = data['Made_or_received_a_digital_payment']
    X = sm.add_constant(X)  # Add a constant for intercept

    # Fit the logistic regression model using sm.Logit
    model = sm.Logit(y, X).fit(disp=0)

    # Save the logistic regression summary
    with open(os.path.join(results_dir, 'logistic_regression_summary.txt'), 'w') as file:
        file.write(model.summary2().as_text())

    # Correlation Matrix
    correlation_matrix = data.corr().round(2)
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.savefig(os.path.join(results_dir, 'correlation_matrix.png'))
    plt.close()

    # Generate Sigmoid Curves for multiple variables in one plot
    plt.figure(figsize=(10, 8))
    for var in [ 'Internet_access','Saved_in_the_past_year']:
        sorted_idx = np.argsort(X[var])
        X_sorted = X.iloc[sorted_idx]
        y_sorted = model.predict(X_sorted)
        plt.plot(X[var].iloc[sorted_idx], y_sorted, label=f'Sigmoid Curve for {var}')

    plt.xlabel('Variable Value')
    plt.ylabel('Probability of Digital Payment')
    plt.title('Multiple Sigmoid Curves')
    plt.legend()
    plt.savefig(os.path.join(results_dir, 'multiple_sigmoid_curves.png'))
    plt.close()

    # Generate ROC Curve and AUC using probabilities from sm.Logit
    y_pred_prob = model.predict(X)
    fpr, tpr, thresholds = roc_curve(y, y_pred_prob)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='blue', label=f'ROC Curve (area = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc='lower right')
    plt.savefig(os.path.join(results_dir, 'roc_curve.png'))
    plt.close()

    # Consolidate all results into a JSON file
    results = {
        'confusion_matrix': confusion_matrix(y, model.predict(X) > 0.5).tolist(),
        'classification_report': classification_report(y, model.predict(X) > 0.5, output_dict=True),
        'roc_auc': roc_auc,
        'correlation_matrix': correlation_matrix.to_dict()
    }
    with open(os.path.join(results_dir, 'evaluation_metrics.json'), 'w') as file:
        json.dump(results, file, indent=4)


if __name__ == "__main__":
    main()
