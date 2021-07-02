import pyupbit
import time
from pandas import DataFrame

def williams(ticker):
    df = pyupbit.get_ohlcv(ticker, interval = "minute30", count = 14)

    cond = df['open'] < df['close']
    u = df[cond]
    d = df[~cond]
    au = sum(u['close'] - u['open']) / len(u)
    ad = sum(d['open'] - d['close']) / len(d)
    rsi = au / (au + ad)

    print(len(u), len(d))
    print(rsi)


williams("KRW-DOGE")