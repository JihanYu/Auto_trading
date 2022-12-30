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
# XRP limit order buy
xrp_price = pyupbit.get_current_price("KRW-XRP")
print(xrp_price)

# 지정가주문을 통해 매매금액보다 낮게 주문
resp = upbit.buy_limit_order("KRW-XRP", 200, 100)   # 티커, 주문가격, 주문량
pprint.pprint(resp)

xrp_balance = upbit.get_balance("KRW-XRP")
resp = upbit.sell_limit_order("KRW-XRP", 265, xrp_balance)  # ticker, price, volume
print(resp)
