import pandas_datareader as pdr
import plotly.graph_objects as go

symbol = 'AAPL' # Please update the symbols here

data = pdr.get_data_yahoo(symbol).reset_index()

print(f"Total records {data.shape[0]}")

print("Taking a peek at the data")

print(data.sort_values('Date', ascending=False).head())

fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])

fig.show()

