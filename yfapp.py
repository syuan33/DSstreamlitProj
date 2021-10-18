import yfinance as yf
import pandas as pd
import streamlit as st

# define the data symbol
tickerOfInterest = "GOOGL"

st.write("""
# Simple Stock price App

Stock closing price of {0}

""".format(tickerOfInterest))

# fatch the data for the symbol
tickerData = yf.Ticker(tickerOfInterest)


# extract the historical data from the ticker object
tickerDF = tickerData.history(period="1d", start='2011-05-31', end='2021-05-31')

st.write("""
```{python}
st.write(tickerDF.head())
```
""")
st.write(tickerDF.head())

# plot

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)
