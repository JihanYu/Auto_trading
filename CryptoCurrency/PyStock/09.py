import pyupbit

import os
path = "C:\\Users\\wocs\\Desktop\\Auto\\CryptoCurrency\\PyStock"
os.chdir(path)

f = open("API.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)     # class instance, object 
balance = upbit.get_balance("KRW")
print(balance)