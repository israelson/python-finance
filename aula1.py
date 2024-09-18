import datetime
import pandas as pd
import yfinance as yf

import plotly.graph_objects as go
import plotly.subplots as make_subplots


ticker = "AAPL"

start = datetime.datetime(2024,1,1)
end = datetime.datetime(2024,9,18)


ticker_ohlc = yf.download(ticker,start,end)

ticker_ohlc['var_close'] = ticker_ohlc['Close'].pct_change(1)

pd.options.display.float_format = '{:.2f}'.format

#print(ticker_ohlc)



#fig = go.Figure(data=[go.Candlestick(x=ticker_ohlc.index,
#                open=ticker_ohlc['Open'],
#                high=ticker_ohlc['High'],
#                low=ticker_ohlc['Low'],
#                close=ticker_ohlc['Close'])])
#
#fig.show()


df_graph = make_subplots()