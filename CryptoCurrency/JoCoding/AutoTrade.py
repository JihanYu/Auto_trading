import time
import pyupbit
import datetime
import os

### Upbit API 를 파일로부터 읽어옴 & Upbit 클래스 객체 생성 ###
def get_upbitAPI(path):
    os.chdir(path)
    f = open("API.txt")
    lines = f.readlines()
    access = lines[0].strip()
    secret = lines[1].strip()
    f.close()
    upbit = pyupbit.Upbit(access, secret)
    return (upbit)

def get_target_price(ticker, k):
    """ 변동성 돌파 전략으로 매수 목표가 조회 """
    df = pyupbit.get_ohlcv(ticker, interval="day", count = 2)   # 최근 2일만 기록 확인
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    # df.iloc[0]이 전일 기록, df.iloc[0]['high'] - df.iloc[0]['low']는 전일 range
    # df.iloc[0]['close']는 금일 시작가와 동일
    return target_price

def get_start_time(ticker):
    """ 시작시간 조회 """
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1) # upbit 에서는 9시를 기준으로 함
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """ 15일 이동평균선 조회 """
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(ticker):
    """ 잔고 조회 """
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """ 현재가 조회 """
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
path = "C:\\Users\\wocs\\Desktop\\Auto\\CryptoCurrency\\PyStock"
upbit = get_upbitAPI(path)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")              # 9:00 AM
        end_time = start_time + datetime.timedelta(days=1)  # 9:00 AM + 1일
        
        # 9:00 < 현재 < 다음날 8:59:50
        if start_time < now < end_time - datetime.timedelta(seconds = 10):
            target_price = get_target_price("KRW-BTC", 0.5)  # <- target price 변화 고려할 수 있음
            ma15 = get_ma15("KRW-BTC")
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
            # if target_price < current_price and ma15 < current_price:
                krw_balance = get_balance("KRW")        # 내 잔고 고려
                if krw_balance > 5000:
                    upbit.buy_market_order("KRW-BTC", krw_balance*0.9995)  # 수수료 0.05%
        
        else:
            ticker_balance = get_balance("KRW-BTC")    # 다음날 8:59:50 일 때
            if ticker_balance > 0.00008:           # 대략 5000원
                upbit.sell_market_order("KRW-BTC", ticker_balance*0.9995)  # 전량 매도, 수수료 0.005%
        time.sleep(1)
        
    except Exception as e:
        print(e)
        time.sleep(1)