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

# 시장가 매수 - 원화 기본
resp = upbit.buy_market_order("KRW-XRP", 10000)   # 티커, 주문가
pprint.pprint(resp)

# 시장가 매도
xrp_balance = upbit.get_balance("KRW-XRP")  # 잔고조회
print(xrp_balance)

resp = upbit.sell_market_order("KRW-XRP", xrp_balance)
print(resp)
