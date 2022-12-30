import pyupbit

df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="week")
df.to_excel("week_btc.xlsx")
print(df)