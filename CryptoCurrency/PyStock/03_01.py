import pyupbit
import pandas as pd

df = pyupbit.get_ohlcv("KRW-BTC", "minute3")
print(df)

def resample(freq = '3T'):
    df = pyupbit.get_ohlcv("KRW-BTC", "minute1")
    
    # resample
    o = df['open'].resample(freq).first()
    h = df['high'].resample(freq).max()
    l = df['low'].resample(freq).min()
    c = df['close'].resample(freq).last()
    v = df['volume'].resample(freq).sum()
    df = pd.concat([o, h, l, c, v], axis=1)
    return df

df = resample('7T')
print(df)
