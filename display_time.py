import sys

def format_time(h, m, s):
    return f"{h:02d}:{m:02d}:{s:02d}"

def print_time(h, m, s):
    sys.stdout.write("\r" + format_time(h, m, s) + "   ")
    sys.stdout.flush()

def input_time():
    """
    Просит у пользователя часы, минуты, секунды.
    Принимает только неотрицательные целые числа.
    Возвращает кортеж (hours, minutes, seconds) с нормализацией.
    """
    def read_component(name):
        while True:
            val = input(f"Введите {name} (число): ").strip()
            if not val.isdigit():
                print("Ошибка: введите неотрицательное целое число.")
                continue
            return int(val)

    h = read_component("часы")
    m = read_component("минуты")
    s = read_component("секунды")

    total = h * 3600 + m * 60 + s
    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60
    return h, m, s
