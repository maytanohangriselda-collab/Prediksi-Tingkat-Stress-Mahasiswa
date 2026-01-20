import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Simulasi hasil encoding dataset Kaggle
data = {
    "academic_pressure": [2,3,4,5,6,7,8,9,10,4,6,8,9,5,7,3,6,10],
    "sleep_hours":       [8,7,6,6,5,5,4,4,3,7,6,5,4,6,5,8,6,3],
    "exam_pressure":     [1,2,3,3,4,4,5,5,5,2,3,4,5,3,4,1,3,5],
    "stress_score":      [1.5,2.0,2.6,3.0,3.5,3.9,4.4,4.8,5.0,
                           2.3,3.2,4.1,4.7,3.1,4.0,1.8,3.4,5.0]
}

df = pd.DataFrame(data)

X = df[["academic_pressure", "sleep_hours", "exam_pressure"]]
y = df["stress_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Test prediction
print(model.predict([[8, 5, 4]]))

# Save model
joblib.dump(model, "stress_prediction_model.pkl")
