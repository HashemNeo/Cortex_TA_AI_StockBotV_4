import streamlit as st
import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
import tempfile


if df is not None:
    # Save the uploaded file to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(df.read())

    # Read the CSV file
    df2 = pd.read_csv(temp_file.name)
    df2.reset_index(inplace=True)
    

st.header('Values Table')
st.dataframe(df2)
st.header('Closing Price Chart')
fig = st.line_chart(df2['Close'])


# Define the LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_size * 2, output_size)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers * 2, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers * 2, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# Load the trained model
model = LSTMModel(input_size=1, hidden_size=32, num_layers=2, output_size=1)
model.load_state_dict(torch.load('trained_model.pth'))
model.eval()

# Define the Streamlit app
def main():
    st.title("Stock Price Prediction App")

    # Add input components
    stock_symbol = st.text_input("Enter stock symbol (e.g., AAPL)")
    num_past_days = st.number_input("Number of past days", min_value=1, max_value=365, value=30)

    if st.button("Predict"):
        # Load historical data
        data = pd.read_csv('stock_data.csv')

        # Filter data for the selected stock symbol
        data = data[data['Symbol'] == stock_symbol]

        # Select the required number of past days
        data = data.tail(num_past_days)

        # Preprocess the data
        prices = data['Close'].values
        min_price = min(prices)
        max_price = max(prices)
        normalized_prices = (prices - min_price) / (max_price - min_price)

        # Convert data into sequences
        sequence_length = 10  # Number of past days to consider for prediction
        sequences = []
        for i in range(len(normalized_prices) - sequence_length):
            sequence = normalized_prices[i:i + sequence_length + 1]
            sequences.append(sequence)

        # Split sequences into input and target
        input_sequences = torch.Tensor([sequence[:-1] for sequence in sequences])
        target_sequences = torch.Tensor([sequence[-1] for sequence in sequences])

        # Create DataLoader
        dataset = StockDataset(input_sequences, target_sequences)
        dataloader = DataLoader(dataset, batch_size=32, shuffle=False)

        # Perform prediction
        predicted_prices = []
        with torch.no_grad():
            for inputs, _ in dataloader:
                outputs = model(inputs.unsqueeze(2))
                predicted_prices.extend(outputs.squeeze().tolist())

        # Denormalize the predicted prices
        predicted_prices = [(price * (max_price - min_price)) + min_price for price in predicted_prices]

        st.subheader("Predicted Closing Prices")
        for i, price in enumerate(predicted_prices):
            st.write(f"Day {i+1}: {price:.2f}")

# Custom Dataset for DataLoader
class StockDataset(Dataset):
    def __init__(self, inputs, targets):
        self.inputs = inputs
        self.targets = targets

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, idx):
        input_data = self.inputs[idx]
        target_data = self.targets[idx]
        return input_data, target_data

if __name__ == '__main__':
    main()
