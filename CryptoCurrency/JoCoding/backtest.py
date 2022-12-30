import pyupbit
import numpy as np

access = "hlbxmWhBueSZLSMsfujcbZy2iKxn7d7pJ02AkliO"
secret = "ZZr1tEfe1TtimIJc5LhC17dwct4dlo7P07bmp3Mz"
upbit = pyupbit.Upbit(access, secret)

## print(upbit.get_balance("KRW-BTC"))
## print(upbit.get_balance("KRW"))

# OHLCV 7일간
df = pyupbit.get_ohlcv("KRW-BTC", count = 7)

# 변동폭 * k 계산, (고가 - 저가) * k 값
df['range'] = (df['high'] - df['low']) * 0.5

# target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shift(1)) - 어제 data를 사용
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0000  # 수수료

# ror(수익률), no.where(조건문, 참일 때 값, 거짓일 때 값)
df['ror'] = np.where(df['high'] > df['target'],         # 고가가 target 보다 높을 때 매수 진행
                     df['close'] / df['target'] - fee,  # 종가에 매도를 하므로 종가/매도가가 수익률
                     1)                                 # 매수가 진행되지 않으면 그대로 있으므로 수익률은 변화 X

# 누적 곱 계산(cumprod) => 누적 수익률
df['hpr'] = df['ror'].cumprod()

# Draw Down 계산(누적최대값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# MDD 계산
print("MDD(%) : ", df['dd'].max())

# excel 로 출력
df.to_excel("dd.xlsx")