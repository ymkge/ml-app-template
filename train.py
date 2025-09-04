import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Ensure the app directory exists
os.makedirs("/Users/ymto/Documents/git/ml-app-template/app", exist_ok=True)

# Load data
df = pd.read_csv("/Users/ymto/Documents/git/ml-app-template/app/data.csv")

# Separate features and target
X = df[['feature1', 'feature2']]
y = df['target']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "/Users/ymto/Documents/git/ml-app-template/app/model.pkl")

print("Model trained and saved to /Users/ymto/Documents/git/ml-app-template/app/model.pkl")
