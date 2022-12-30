import pyupbit
import pprint

import os
path = "C:\\Users\\wocs\\Desktop\\Auto\\CryptoCurrency\\PyStock"
os.chdir(path)

f = open("API.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)

df = pyupbit.get_ohlcv("KRW-BTC", interval="day", count=200)
print(df.head())
df.to_excel("btc.xlsx")