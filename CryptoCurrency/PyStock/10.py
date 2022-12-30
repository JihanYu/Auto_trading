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
balances = upbit.get_balances()
pprint.pprint(balances)

balance = upbit.get_balance(ticker="KRW")
print(balance)