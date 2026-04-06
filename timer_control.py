import time
from display_time import print_time

def countdown(h, m, s):
    total = h * 3600 + m * 60 + s
    try:
        while total > 0:
            hh = total // 3600
            mm = (total % 3600) // 60
            ss = total % 60

            print_time(hh, mm, ss)
            time.sleep(1)
            total -= 1

        print_time(0, 0, 0)
        print()
        print("Время истекло!")
    except KeyboardInterrupt:
        print("\nТаймер остановлен пользователем.")
