from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import date
import yfinance as yf
import streamlit as st
import plotly
import pandas as pd
import tempfile

start = '2015-01-01'
today = date.today().strftime("%Y-%m-%d")

st.title("Future Prediction  ❤️")

df2 = st.file_uploader("Choose a CSV file", type="csv")
n_years = st.slider("years of prediction:",1,4)
period = n_years* 365

if df2 is not None:
    # Save the uploaded file to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(df2.read())
    # Read the CSV file
    df2 = pd.read_csv(temp_file.name)
    df2.reset_index(inplace=True)
    

st.header('Values Table')
df2.set_index('Date', inplace=True)
st.dataframe(df2)
st.header('Closing Price Chart')
fig = st.line_chart(df2['Close'])

st.subheader('Raw dataframe')
st.write(df2.tail())

fig = go.Figure()
fig.add_trace(go.Scatter(x=df2['Date'], y=df2['Open'], name='stock_open'))
fig.add_trace(go.Scatter(x=df2['Date'], y=df2['Close'], name='stock_close'))
fig.layout.update(title='Time Series df2',xaxis_rangeslider_visible=True)
st.plotly_chart(fig)




#Hashem
#Forcasting
df_train = df2[['Date','Close']]
df_train = df_train.rename(columns={"Date": 'ds', 'Close': 'y'})

m = Prophet()
m.fit(df_train)
future = m.make_future_df2frame(periods=period)

forcast = m.predict(future)

st.subheader('forcast df2')
st.write(forcast.tail())

fig1 = plot_plotly(m, forcast)
st.plotly_chart(fig1)

st.write('forcast components')
fig2 = m.plot_components(forcast)

st.write(fig2)






