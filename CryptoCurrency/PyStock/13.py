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
resp = upbit.buy_limit_order("KRW-XRP", 200, 100)
pprint.pprint(resp)

################
# uuid 로 취소 #
################

uuid = resp[0]['uuid']

resp = upbit.cancel_order(uuid=uuid)  # resp[0]['uuid']
print(resp)

