import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
data = pd.read_csv("your_dataset.csv")
data = data.drop(columns=['unnecessary_column'])
data =data.dropna()data = pd.get_dummies(data, drop_first=True)
X = data.drop("target_column", axis=1)
y = data["target_column"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")
print("Predictions:", predictions[:10])