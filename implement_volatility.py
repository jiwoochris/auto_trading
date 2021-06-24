from volatility import *

with open("upbit_key.txt", "r") as f:
    key1 = f.readline().srtip()
    key2 = f.readline().srtip()

upbit = pyupbit.Upbit(key1, key2)
target_price = get_target_price()

hold_flag = False # 매수 했다면 True, 그렇지 않다면 False

while True:
    
    now = datetime.datetime.now()
    mid = datetime.datetime(now.year, now.month, now.day) # 자정
    delta = datetime.timedelta(seconds = 10)

    if mid <= now <= mid + delta:
        if hold_flag == True:
            ret = sell_crypto_currency(upbit)
            ret = upbit.get_order(ret)
            print("매도", ret)
        target_price = get_target_price()
        hold_flag = False

    else:
        price = pyupbit.get_current_price("KRW-BTC")
        if target_price <= price and hold_flag == False:
            ret = buy_crypto_currency(upbit, price)
            print("매수", ret)
            hold_flag = True

    
    print(now, target_price, price)

    time.sleep(1)