import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

import joblib

fuelData = pd.read_csv("Fuel-prediction/fuelData.csv")

# print(fuelData.head())

# print("\n Columns: \n", fuelData.columns)

features = [
    'Engine size (L)',
    'Cylinders',
    'City (L/100 km)',
    'Highway (L/100 km)'
]

X  = fuelData[features]
Y = fuelData["Combined (L/100 km)"]

# print(X.head())
# print(Y.head())

X_train , X_test , Y_train , Y_test = train_test_split(
    X , Y , test_size = 0.2 , random_state=42
)

model = LinearRegression()
model.fit(X_train, Y_train)

predictY = model.predict(X_test)

score = r2_score(Y_test, predictY)
print("R**2 score:", score)

sample = pd.DataFrame([[2.0, 4, 9.5, 7]], columns = ['Engine size (L)', 'Cylinders','City (L/100 km)','Highway (L/100 km)']) #engineSize=2L,no. of cylinders=4

prediction = model.predict(sample)

print("Predicted fuel consumption:", prediction[0])

joblib.dump(model, "model.pkl")
print("model saved!")