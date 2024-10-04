# Secondamer

import time
hour = 0
minut = 0
second = 0

while True:
    time.sleep(1)
    second += 1
    if second >= 59:
        second = 0
        minut += 1
        if minut >= 59:
            minut = 0
            hour += 1

    print(f'{hour}:{minut}:{second}')