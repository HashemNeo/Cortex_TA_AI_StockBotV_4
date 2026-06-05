from plotly import graph_objs as go
from datetime import date
import time
import random
import streamlit as st
import plotly
import pandas as pd
import tempfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pkg_resources
import types

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



