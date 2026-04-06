from display_time import input_time
from timer_control import countdown

def main():
    print("Введите время таймера (часы, минуты, секунды). Только числа.")
    h, m, s = input_time()
    print("Запуск таймера...")
    countdown(h, m, s)

if __name__ == "__main__":
    main()
