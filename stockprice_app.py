import yfinance as yf
import streamlit as st

st.write("""
## Simple stock price app

Shown are the stock **closing price** and **volume** of Google

""")

# define the ticker symbol
tickerSymbol = 'GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2010-1-1', end='2022-12-31')
st.write("""
### Closing price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume
""")
st.line_chart(tickerDf.Volume)