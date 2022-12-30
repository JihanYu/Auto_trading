import pyupbit
import pprint

orderbooks = pyupbit.get_orderbook("KRW-BTC")
pprint.pprint(orderbooks)

# orderbook = orderbooks[0]

total_ask_size = orderbooks['total_ask_size']
total_bid_size = orderbooks['total_bid_size']

print("total ask : ", total_ask_size)
print("total bid : ", total_bid_size)

