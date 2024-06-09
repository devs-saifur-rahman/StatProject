import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
csv_file_path = 'Pre-Processed-Data.csv'  # Replace with the actual path to your CSV file
data = pd.read_csv(csv_file_path)

# Display the first few rows and columns to understand its structure
print("First few rows of the dataset:")
print(data.head())
print("\nColumns in the dataset:")
print(data.columns.tolist())

# Encode categorical variables using LabelEncoder
label_encoders = {}
for column in ['Income Quality', 'Made or received a digital payment']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column].astype(str))
    label_encoders[column] = le

# Define the dependent variable
dependent_var = 'Made or received a digital payment'

# Define the independent variable
independent_var = 'Income Quality'

# Prepare the X (independent variable) and y (dependent variable)
X = data[[independent_var]]
y = data[dependent_var]

# Add a constant to the model (intercept)
X = sm.add_constant(X)

# Fit the logistic regression model
logit_model = sm.Logit(y, X).fit()

# Display the logistic regression summary
print("\nLogistic Regression Summary:")
print(logit_model.summary())

# Predict the probabilities
y_pred_prob = logit_model.predict(X)

# Classify based on a threshold of 0.5
y_pred = (y_pred_prob >= 0.5).astype(int)

# Confusion Matrix
cm = confusion_matrix(y, y_pred)

# ROC Curve
fpr, tpr, _ = roc_curve(y, y_pred_prob)
roc_auc = auc(fpr, tpr)

# Plot Confusion Matrix
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
plt.title('Confusion Matrix for Digital Payment Prediction')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

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
plt.show()

# Sigmoid Curve for Income_Quality
Income_Quality_values = np.sort(data[independent_var].unique())
X_test = pd.DataFrame({independent_var: Income_Quality_values})
X_test = sm.add_constant(X_test)
y_test_pred_prob = logit_model.predict(X_test)

plt.figure(figsize=(10, 7))
plt.plot(Income_Quality_values, y_test_pred_prob, color='red', linewidth=3)
plt.scatter(data[independent_var], y, color='black', zorder=20, alpha=0.5)
plt.xlabel('Income Quality')
plt.ylabel('Probability of Digital Payment')
plt.title('Logistic Regression Sigmoid Curve for Income Quality')
plt.show()
