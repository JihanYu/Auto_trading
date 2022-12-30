import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", "minute3")
print(df)

df['open'].resample('3T').first()
df['high'].resample('3T').max()
df['low'].resample('3T').min()
df['close'].resample('3T').last()
df['volume'].resample('3T').sum()
