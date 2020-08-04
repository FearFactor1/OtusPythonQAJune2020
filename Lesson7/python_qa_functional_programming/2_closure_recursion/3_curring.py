from functools import partial


# Каррирование (от англ. currying, иногда — карринг) — преобразование функции от многих аргументов в набор функций,
# каждая из которых является функцией от одного аргумента.

def time_tracking(start, dest, speed):
    """Функция рассчёта времени из точки а в точку б"""
    return abs((dest - start) / speed)


MOSCOW = 1000
VLADIVOSTOK = 9000
CAR_SPEED = 60

form_moscow = partial(time_tracking, start=MOSCOW)

print(form_moscow(dest=VLADIVOSTOK, speed=CAR_SPEED))