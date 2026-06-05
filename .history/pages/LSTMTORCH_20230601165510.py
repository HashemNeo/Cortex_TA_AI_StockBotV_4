import streamlit as st
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import tempfile
from sklearn.preprocessing import MinMaxScaler


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



# Set up the Streamlit app
st.title('Stock Price Forecasting with LSTM')

# Prepare the data
data = df['Close'].values.reshape(-1, 1)

The error indicates a mismatch between the input size of the model and the provided data. The model expects an input size of 1, but it seems the provided data has a different shape.

To resolve this issue, you need to ensure that the input data has the correct shape and size. Specifically, the LSTM model in this example expects a sequence of 30 previous time steps as input, each with a single feature. Here's an updated version of the code:

```python
# ...

# Split the data into training and testing sets
train_data = scaled_data[:-num_time_steps]
test_data = scaled_data[-num_time_steps:]

# Convert the training data into sequences of 30 time steps
def create_sequences(data, seq_length):
    sequences = []
    for i in range(len(data) - seq_length):
        sequence = data[i : i + seq_length]
        sequences.append(sequence)
    return sequences

train_sequences = create_sequences(train_data, num_time_steps)
train_sequences = torch.FloatTensor(train_sequences)

# ...

# Define the LSTM model
class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(LSTM, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size)
        self.fc = nn.Linear(hidden_size, output_size)
        
    def forward(self, input):
        lstm_out, _ = self.lstm(input.view(len(input), 1, -1))
        prediction = self.fc(lstm_out.view(len(input), -1))
        return prediction[-1]

# ...

# Create an instance of the LSTM model
input_size = 1
hidden_size = 32
output_size = 1
model = LSTM(input_size, hidden_size, output_size)

# ...

# Train the LSTM model
num_epochs = 100
learning_rate = 0.001

criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    
    output = model(train_sequences)
    loss = criterion(output, train_sequences)
    
    loss.backward()
    optimizer.step()
    
    if (epoch+1) % 10 == 0:
        print(f'Epoch: {epoch+1}/{num_epochs}, Loss: {loss.item()}')

# Save the trained model
torch.save(model.state_dict(), 'lstm_model.pt')


# Load the trained model weights
model.load_state_dict(torch.load('lstm_model.pt'))

# Set the model to evaluation mode
model.eval()

# Predict the next day's close price
with torch.no_grad():
    input = test_data
    predictions = []
    for i in range(num_time_steps):
        input = input.view(1, -1)
        output = model(input)
        predictions.append(output.item())
        input = torch.cat((input[1:], output))

# Scale the predicted values back to the original range
predicted_prices = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

# Plot the actual and predicted prices
fig, ax = plt.subplots()
ax.plot(df['Date'][-num_time_steps:], test_data.numpy(), label='Actual')
ax.plot(df['Date'][-num_time_steps:], predicted_prices, label='Predicted')
ax.set_xlabel('Date')
ax.set_ylabel('Closing Price')
ax.set_title('Stock Price Forecast using LSTM')
ax.legend()
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)
