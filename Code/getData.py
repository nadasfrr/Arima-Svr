import pandas
import yfinance as yf
from datetime import timedelta, date
btc = yf.Ticker('BTC-USD')

start = date(2021, 6, 6)
end = date(2022, 6, 6)
print(start, end)
data = yf.download("BTC-USD", start=start, end=end)

df = pandas.DataFrame(data=data)

df.to_csv('Dataset/BTC-USD.csv')
