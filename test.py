import pyupbit
from pandas import DataFrame

df = pyupbit.get_ohlcv("KRW-BTC", interval = "minute5", to = "202006282005")

for i in range(len(df)):
    if(i>3):
        print(df.iloc[i-3]['open'])