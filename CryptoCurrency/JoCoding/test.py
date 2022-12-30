import pyupbit
access = "hlbxmWhBueSZLSMsfujcbZy2iKxn7d7pJ02AkliO"
secret = "ZZr1tEfe1TtimIJc5LhC17dwct4dlo7P07bmp3Mz"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))
print(upbit.get_balance("KRW"))
