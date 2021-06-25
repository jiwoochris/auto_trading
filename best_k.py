import pyupbit
import time
from pandas import DataFrame

def williams(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval = "minute10", count= 30)

    range = (df['high'] - df['low']) * k
    target = df['open'] + range.shift(1)

    cond = df['high'] > target
    buy = target[cond]
    sell = df['close'][cond]

    rate = sell / buy

    print(k, rate)
    if rate.empty:
        return 0
    else:
        return rate.cumprod().iloc[-1] * (0.9995 ** len(rate) )

data = []
for k in range(1, 21):
    data.append([k/10, williams("KRW-DOGE", k/10)])
    time.sleep(0.1)

df = DataFrame(data)
df.columns = ["k", "return rate"]

print(df.sort_values('return rate'))