import pyupbit
from pandas import DataFrame

df = pyupbit.get_ohlcv("KRW-BTC", interval = "minute5", to = "202006282005")

for i in range(len(df)):
    if(i>3):
        if df.iloc[i-4]['open'] < df.iloc[i-4]['close'] and df.iloc[i-3]['open'] > df.iloc[i-3]['close'] and df.iloc[i-2]['open'] > df.iloc[i-2]['close'] and df.iloc[i-1]['open'] > df.iloc[i-1]['close']:
            min = min([num(df.iloc[i-3]['volume']), float(df.iloc[i-2]['volume']), float(df.iloc[i-1]['volume'])])
            print(min)