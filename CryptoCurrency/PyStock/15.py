import pyupbit
import time
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

### 목표가 구함 ###
def cal_target(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day")
    yesterday = df.iloc[-2]     ## 행 마지막에서 바로 위
    today = df.iloc[-1]         ## 행 마지막
    yesterday_range = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterday_range * k
    return(target)

path = "C:\\Users\\wocs\\Desktop\\Auto\\CryptoCurrency\\PyStock"
upbit = get_upbitAPI(path)

k = 0.5
target = cal_target("KRW-BTC", k)

# 매수기능 추가 - 프로그램을 처음 시작한 날은 매수되지 않도록 처리
#    - 현재가가 목표가보다 한참 위에 있을 때 매수가 될 수 있기 때문
op_mode = False

## 매수기능 추가
## 보유 상태를 False 로 설정 (현재 가지고 있는지를 설정)
hold = False    # 초기 선언이므로 False (처음에는 가지고 있지 않음)

while True:
    now = datetime.datetime.now()

    #####  매도기능 추가 #####
    # - 매도 시도 - 08:59:00에 보유하고 있다면 전량 매도
    # 8:59:50 - 09:00:00 에 매도
    if now.hour == 8 and now.minute == 59 and (50 <= now.second <= 59):
        if op_mode is True and hold is True:
            ticker_balance = upbit.get_balance("KRW-BTC")
            upbit.sell_market_order("KRW-BTC", ticker_balance)
            hold = False
        
        # 새로운 거래일에서 목표가 갱신될 때까지 거래가 되지 않도록 함
        op_mode = False
        time.sleep(10)      # 다음날 목표가 갱신될 때까지 잠깐 기다려라.
    
    #####  목표가 갱신 #####
    # 목표가 갱신 (매일 아침 9시 이후 목표가 갱신이 필요) - 9시 이후 첫 거래가 일어난 후 계산되어야 함
    # 9:00:20 - 9:00:30 
    if now.hour == 9 and now.minute == 0 and (20 <= now.second <= 30):
        target = cal_target("KRW-BTC", k)
        time.sleep(10)          # 9:00:20 - 9:00:30 간격에서는 연속 계산하지 않음
        op_mode = True          # 프로그램 시작 다음날부터 매매 가능으로 변경
        
    price = pyupbit.get_current_price("KRW-BTC")

    ##### 매수기능 추가 #####
    # 매초마다 조건을 확인 후 매수 시도
    if op_mode is True and price is not None and price >= target and hold is False:
        # (현재 사도 좋다(op_mode), 현재가가 목표가보다 높음, 현재 가지고 있지 않음(hold)
        # price is not None : 가격이 구해지지 않을 때 에러가 날 수 있음 / 가격이 구해질 경우에만 code 돌아가도록 함
        krw_balance = upbit.get_balance("KRW")
        upbit.buy_market_order("KRW-BTC", krw_balance)      # 시장가 구매, 잔고(krw_balance) 전체로 구입
        hold = True     # 보유가 되면 True 로 변경 (hold True) (한번 사면 다시 안살거다)

    ##### 상태 출력 #####
    # - 현재 시간, 목표가, 현재가, 보유상태, 동작상태 출력
    print(f"현재시간 {now}, 목표가: {target}, 현재가: {price}, 보유상태: {hold}, 동작상태: {op_mode}")
    
    time.sleep(1)