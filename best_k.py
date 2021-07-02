import pyupbit
import time
from pandas import DataFrame

def williams(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval = "minute240", count = 42)

    range = (df['high'] - df['low']) * k
    target = df['open'] + range.shift(1)

    cond = df['high'] >= target
    buy = target[cond]
    sell = df['close'][cond]

    rate = sell / buy

    origin = df['close'][-1] / df['open'][0]


    print(k, rate)
    print("origin :", 0.999 * origin)
    if rate.empty:
        return 0
    else:
        return rate.cumprod().iloc[-1] * (0.999 ** len(rate) )
    

data = []
for k in range(1, 21):
    data.append([k/10, williams("KRW-MLK", k/10)])
    time.sleep(0.1)

df = DataFrame(data)
df.columns = ["k", "return rate"]

print(df.sort_values('return rate'))