from prophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import date
import streamlit as st
import plotly
import pandas as pd
import tempfile
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.losses import MeanSquaredError




start = '2015-01-01'
today = date.today().strftime("%Y-%m-%d")

st.title("Future Prediction #2 ❤️")

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

# Convert the 'Date' column to datetime if it's not already in the correct format
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date in ascending order
df = df.sort_values('Date')

# Normalize the 'Close' column between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
df['Close'] = scaler.fit_transform(df['Close'].values.reshape(-1, 1))


# Extract the 'Close' column as the target variable
target = df['Close'].values

# Create a lagged representation of the 'Close' column to use as input features
lagged_data = np.array([target[i:i+14] for i in range(len(target)-14)])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(lagged_data[:, :-1], lagged_data[:, -1], test_size=0.2, shuffle=False)


X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))


model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(X_train.shape[1], 1)))
model.add(LSTM(50, activation='relu', input_shape=(X_train.shape[1], 1)))
model.add(LSTM(50, activation='relu', input_shape=(X_train.shape[1], 1)))
model.add(LSTM(25, activation='relu', input_shape=(X_train.shape[1], 1)))
model.add(Dense(1))


model.compile(optimizer='adam', loss=MeanSquaredError())


model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)


loss = model.evaluate(X_test, y_test)
print(f"Test loss: {loss}")


# Assuming you have already trained and saved your model
predictions = model.predict(X_test)

# Rescale the predicted values back to the original range
predictions = scaler.inverse_transform(predictions)


# Create a list of dates for the next 14 days
next_14_days = pd.date_range(df['Date'].max(), periods=14).tolist()

# Prepare the data for the diagram
x_values = next_14_days
y_values = predictions.flatten()

# Plot the data
plt.plot(x_values, y_values)
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Predicted Closing Prices for the Next 14 Days')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot in Streamlit
st.pyplot(plt)
