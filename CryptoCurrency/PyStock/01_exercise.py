import requests

url = "https://api.upbit.com/v1/market/all"
params = {
    "isDetails" : "false"
}

resp = requests.get(url, params = params)
data = resp.json()
print(data)

krw_tickers = []
for coin in data:
    ticker = coin['market']     # coin = dict type  -   market 을 통해 접근 
    
    if ticker.startswith("KRW"):  # "KRW-BTC" 의 형식을 선택함
        krw_tickers.append(ticker)
    
print(krw_tickers)
print(len(krw_tickers))
    