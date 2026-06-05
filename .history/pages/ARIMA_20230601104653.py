import streamlit as st
from datetime import datetime, date
import tempfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load the stock price data from a CSV file
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

st.header('Values Table')
st.dataframe(df)
st.header('Closing Price Chart')
fig = st.line_chart(df['Close'])


# Set up the Streamlit app
st.title('Stock Price Forecasting with ARIMA')

# Display the loaded data
st.subheader('Stock Price Data')
st.write(df)

# Fit and forecast using ARIMA
def fit_arima(df):
    # Convert 'Date' column to datetime and set it as index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Fit ARIMA model
    model = ARIMA(df['Close'], order=(1, 1, 1))
    model_fit = model.fit()

    # Forecast next 14 days
    forecast = model_fit.predict(start=len(df), end=len(df) + 13)

    return forecast

forecast = fit_arima(df)

# Plot the forecasted values
st.subheader('Forecasted Stock Prices for the Next 14 Days')
plt.plot(df.index, df['Close'], label='Actual')
plt.subplots(figsize=(20, 14))
plt.plot(pd.date_range(start=df.index[-1], periods=14), forecast, label='Forecasted')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Price Forecast')
plt.legend()
plt.xticks(rotation=45)
st.pyplot(plt)
