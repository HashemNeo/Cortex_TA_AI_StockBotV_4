import numpy as np
import pandas as pd
import streamlit as st
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

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

