import time
import datetime

while True:
    now = datetime.datetime.now()
    if now.minute % 2 == 1:
        print("odd minute")
        print(now)
    else:
        if 0 <= now.second <= 10:
            print("special")
        print("even minute")
        print(now)

    time.sleep(1)