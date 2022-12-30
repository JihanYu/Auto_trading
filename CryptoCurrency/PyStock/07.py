import pyupbit

price = pyupbit.get_current_price("KRW-BTC")
print(price)

tickers = ["KRW-BTC", "KRW-XRP"]
price = pyupbit.get_current_price(tickers)
print(price)
