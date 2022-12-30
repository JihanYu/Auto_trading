import pyupbit

krw_tickers = pyupbit.get_tickers(fiat="KRW")
# print(krw_tickers)

prices = pyupbit.get_current_price(krw_tickers)
# print(prices)

for k, v in prices.items():
    print(k, v)