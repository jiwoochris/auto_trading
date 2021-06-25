from vol_k_05_doge import *

with open("upbit_key.txt", "r") as f:
    key1 = f.readline().strip()
    key2 = f.readline().strip()

upbit = pyupbit.Upbit(key1, key2)
target_price = get_target_price()

hold_flag = False # 매수 했다면 True, 그렇지 않다면 False

while True:
    
    now = datetime.datetime.now()

    if now.minute % 30 == 0 and 0 <= now.second <= 10:
        if hold_flag == True:
            ret = sell_crypto_currency(upbit)
            ret = upbit.get_order(ret)
            print("매도", ret)
        target_price = get_target_price()
        hold_flag = False

    else:
        price = pyupbit.get_current_price("KRW-DOGE")
        if target_price <= price and hold_flag == False:
            ret = buy_crypto_currency(upbit, price)
            print("매수", ret)
            hold_flag = True

    print(now, target_price, price)

    time.sleep(1)