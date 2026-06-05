from plotly import graph_objs as go
from datetime import date
import streamlit as st
import pandas as pd
import tempfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
sns.set()


start = '2015-01-01'
today = date.today().strftime("%Y-%m-%d")

st.title("Buy&Sell Prediction ❤️")

df = st.file_uploader("Choose a CSV file", type="csv")

if df is not None:
    # Save the uploaded file to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(df.read())

    # Read the CSV file
    df = pd.read_csv(temp_file.name)
    df.set_index('Date', inplace=True)

st.header('Values Table')
st.dataframe(df)
st.header('Closing Price Chart')
fig = st.line_chart(df['Close'])





# Load the stock price data from a CSV file
df = pd.read_csv('stock_prices.csv')

# Prepare the data
X = df[['Volume', 'Open', 'High', 'Low']]  # Input features
y = df['Close']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the Random Forest Regression model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Evaluate the model
mse_train = mean_squared_error(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)

# Print the mean squared error
print('Mean Squared Error (Train):', mse_train)
print('Mean Squared Error (Test):', mse_test)

# Plot the actual and predicted values
plt.plot(df.index, df['Close'], label='Actual')
plt.plot(df.index[X_train.index], y_pred_train, label='Predicted (Train)')
plt.plot(df.index[X_test.index], y_pred_test, label='Predicted (Test)')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Price Forecast using Random Forest Regression')
plt.legend()
plt.xticks(rotation=45)
plt.show()
