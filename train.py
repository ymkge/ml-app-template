import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
from pathlib import Path

# Get the project root directory (where train.py is located)
# This makes the script runnable from anywhere.
project_root = Path(__file__).parent

# Define paths relative to the project root
app_dir = project_root / "app"
data_path = app_dir / "data.csv"
model_path = app_dir / "model.pkl"

# Ensure the app directory exists
app_dir.mkdir(exist_ok=True)

# Load data
df = pd.read_csv(data_path)

# Separate features and target
X = df[['feature1', 'feature2']]
y = df['target']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, model_path)

print(f"Model trained and saved to {model_path}")
