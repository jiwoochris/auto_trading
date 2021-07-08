from jmod2 import *

with open("upbit_key.txt", "r") as f:
    key1 = f.readline().strip()
    key2 = f.readline().strip()

upbit = pyupbit.Upbit(key1, key2)

ticker_list = ["KRW-ETH", "KRW-ETC", "KRW-HUNT", "KRW-XRP", "KRW-DOGE", "KRW-BCH", "KRW-DAWN", "KRW-RFR", "KRW-META", "KRW-FCT2"]

hold_flag = False # 매수 했다면 True, 그렇지 않다면 False

post_message("Start coin auto trading program for jiwoo.")

while True:
    
    now = datetime.datetime.now()
    
    if now.hour % 4 == 1 and now.minute == 0 and 1 <= now.second <= 10:
        ticker_list = ["KRW-ETH", "KRW-ETC", "KRW-HUNT", "KRW-XRP", "KRW-DOGE", "KRW-BCH", "KRW-DAWN", "KRW-RFR", "KRW-META", "KRW-FCT2"]

    else:
        if hold_flag == False:
            signal_ticker = get_signal(ticker_list)
            
            ret = buy_crypto_currency(upbit, signal_ticker)
            print("매수", ret)
            post_message(f"[Jiwoo][매수] {ret['market']} {ret['price']}")
            ticker_list.remove(signal_ticker)
            hold_flag = True

        if hold_flag == True:
            before = upbit.get_balance("KRW")
            ret = sell_crypto_currency(upbit, signal_ticker)
            print("매도", ret)
            post_message(f"[Jiwoo][매도] {ret['market']} {ret['price']}")
            krw = upbit.get_balance("KRW")
            if krw > before:
                결과 = "이득"
            else:
                결과 = "손해"
            수익률 = krw / before * 100 -100

            post_message(f"[Jiwoo][{결과}] {수익률} % 잔고 : {krw}")
            hold_flag = False

    time.sleep(0.1)