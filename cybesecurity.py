import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
# Assume 'data.csv' contains network traffic data with features for analysis
data = pd.read_csv('data.csv')

# Preprocess data: selecting relevant features (update based on your dataset)
features = ['feature1', 'feature2', 'feature3']  # Replace with actual feature names
X = data[features]

# Split data into training and test sets
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Define and train Isolation Forest model
model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(X_train)

# Predict anomalies on test data
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Convert prediction labels (-1 for anomaly, 1 for normal) to binary labels (1 for anomaly, 0 for normal)
y_pred_train = np.where(y_pred_train == -1, 1, 0)
y_pred_test = np.where(y_pred_test == -1, 1, 0)

# Evaluate model
print("Accuracy on test data:", accuracy_score([0]*len(y_pred_test), y_pred_test))
print("Classification Report:\n", classification_report([0]*len(y_pred_test), y_pred_test))

# Identify anomalies
anomalies = X_test[y_pred_test == 1]
print("Detected anomalies:\n", anomalies)
