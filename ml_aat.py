# -*- coding: utf-8 -*-
"""ML_AAT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K5C65X8UsuuH8eEZ4WItgfRQcolyrhok
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
file_path = 'WineQT.csv'
data = pd.read_csv(file_path)
data

# Check for missing values
print(data.isnull().sum())

# Preprocess data
X = data.drop('quality', axis=1)
y = data['quality']

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Function to evaluate model performance
def evaluate_model(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    cm = confusion_matrix(y_test, y_pred)

    print(f'Accuracy: {accuracy}')
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1 Score: {f1}')
    print('Confusion Matrix:')
    print(cm)

    # Plot confusion matrix
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

# Return the preprocessed data for further use
X_train, X_test, y_train, y_test

"""# **LOGISTIC REGRESSION MODEL**"""

from sklearn.linear_model import LogisticRegression

# Train logistic regression model
log_reg_model = LogisticRegression(max_iter=1000, random_state=42)
log_reg_model.fit(X_train, y_train)

# Predict and evaluate
y_pred_log_reg = log_reg_model.predict(X_test)
print("Logistic Regression:")
log_reg_evaluation = evaluate_model(y_test, y_pred_log_reg)
log_reg_evaluation

"""# DECISON TREE MODEL

"""

from sklearn.tree import DecisionTreeClassifier

# Train decision tree model
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)

# Predict and evaluate
y_pred_tree = tree_model.predict(X_test)
print("Decision Tree:")
evaluate_model(y_test, y_pred_tree)

"""# RANDOM FOREST"""

from sklearn.ensemble import RandomForestClassifier

# Train random forest model
forest_model = RandomForestClassifier(n_estimators=100, random_state=42)
forest_model.fit(X_train, y_train)

# Predict and evaluate
y_pred_forest = forest_model.predict(X_test)
print("Random Forest:")
evaluate_model(y_test, y_pred_forest)

"""# SUPPORT VECTOR MACHINE (SVM)"""

from sklearn.svm import SVC

# Train SVM model
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

# Predict and evaluate SVM
y_pred_svm = svm_model.predict(X_test)
print("SVM:")
svm_evaluation = evaluate_model(y_test, y_pred_svm)
svm_evaluation

"""# VISUALISATION

FN: The False-negative value for a class will be the sum of values of corresponding rows except for the TP value.

FP: The False-positive value for a class will be the sum of values of the corresponding column except for the TP value.

TN: The True-negative value for a class will be the sum of the values of all columns and rows except the values of that class that we are calculating the values for. And

TP: the True-positive value is where the actual value and predicted value are the same.

```
         Predicted
         1    2    3    4    5
Actual  ----------------------
1       TN   FP   FP   FP   FP
2       FN   TP   FP   FP   FP
3       FN   FN   TP   FP   FP
4       FN   FN   FN   TP   FP
5       FN   FN   FN   FN   TP
```

### Accuracy: 0.64

The proportion of correctly classified instances out of the total instances.

### Precision: 0.62

The proportion of true positive predictions out of all positive predictions.

### Recall: 0.64
The proportion of true positive predictions out of all actual positive instances.

### F1 Score: 0.63
The harmonic mean of precision and recall.

## Confusion Matrix:

The confusion matrix is a table used to describe the performance of a
classification model.
Each row represents the instances in an actual class, while each column represents the instances in a predicted class.

In this matrix:
*   The rows represent the actual classes (from 1 to 5).
*   The columns represent the predicted classes (from 1 to 5).
*   The entry in row 'i' and column 'j' represents the number of instances of class 'i' that were predicted as class 'j'.
*   For example, the entry in row 2, column 3 (23) means there are 23 instances of class 2 predicted as class 3.
"""