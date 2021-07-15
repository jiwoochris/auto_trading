import pyupbit
import time
import pandas as pd
from datetime import datetime

now = datetime.now()

start = "20210701"
last = now

dfs = []

while True:
    df = pyupbit.get_ohlcv("KRW-ETH", interval = "minute15", to = last)
    last = df.index[0]

    dfs.append(df)

    time.sleep(0.1)

    if start in df.index:
        break

result = pd.concat(dfs).sort_index()
result = result.loc[ start : ]
result = pd.DataFrame(result)

#print(result)

CV = result['close'] * result['volume']
VWMA_5 = CV.rolling(5).sum() / result['volume'].rolling(5).sum()
VWMA_10 = CV.rolling(10).sum() / result['volume'].rolling(10).sum()
VWMA_25 = CV.rolling(25).sum() / result['volume'].rolling(25).sum()

VPC = VWMA_25 - result['close'].rolling(25).mean()
VPR = VWMA_5 / result['close'].rolling(5).mean()
VM = result['volume'].rolling(5).mean() / result['volume'].rolling(25).mean()
VPCI = VPC * VPR * VM
VPCIS_5 = VPCI.rolling(5).mean()
VPCIS_20 = VPCI.rolling(20).mean()
result['VPCI'] = VPCI
result['VPCIS_5'] = VPCIS_5
result['VPCIS_20'] = VPCIS_20

result['VW_dis'] = result['close'] / VWMA_25 * 100
#print(result['VW_dis'].rolling(20).mean())

cond1 = (result['VW_dis'].shift(1) < 99) & (result['high'].shift(1) - result['open'].shift(1) < result['close'].shift(1) - result['open'].shift(1)) & (result['close'].shift(1) - result['open'].shift(1) < result['open'].shift(1) - result['low'].shift(1)) & (result['volume'].shift(2) * 2 < result['volume'].shift(1))
buy1 = result['open'][cond1]

cond2 = (result['VW_dis'].shift(1) > 101) & (result['high'].shift(1) - result['open'].shift(1) < result['close'].shift(1) - result['open'].shift(1)) & (result['close'].shift(1) - result['open'].shift(1) > result['open'].shift(1) - result['low'].shift(1)) & (result['volume'].shift(2) * 2 < result['volume'].shift(1))
buy2 = result['open'][cond2]

print(buy1)
#buy2.to_excel("BTC2.xlsx")
print(buy2)