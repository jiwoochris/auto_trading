import pyupbit
from pandas import DataFrame

df = pyupbit.get_ohlcv("KRW-ETH", interval = "minute5")

for i in range(len(df)):
    if(i>3):
        if df.iloc[i-4]['open'] < df.iloc[i-4]['close'] and df.iloc[i-3]['open'] > df.iloc[i-3]['close'] and df.iloc[i-2]['open'] > df.iloc[i-2]['close'] and df.iloc[i-1]['open'] > df.iloc[i-1]['close']:
            if df.iloc[i-4]['volume']*1.4 < df.iloc[i-3]['volume'] and df.iloc[i-4]['volume']*1.4 < df.iloc[i-2]['volume'] and df.iloc[i-4]['volume']*1.4 < df.iloc[i-1]['volume']:
                if df.iloc[i-4]['volume']*2.5 > df.iloc[i-3]['volume'] or df.iloc[i-4]['volume']*2.5 > df.iloc[i-2]['volume'] or df.iloc[i-4]['volume']*2.5 > df.iloc[i-1]['volume']:
                    print(df.iloc[i])
                    print(df.iloc[i]['close'] / df.iloc[i]['open'])