# Функция с двумя аргументами, один задан по умолчанию
def foo(a, b=1):
    return a + b


# Функция принимающая любое количество неименованных аргументов
print("Любое количество позиционных аргументов")


def any_args(*args):
    print(args)


any_args(1, 2, 3, 4)

# Функция принимающая любое количество именованных аргументов
print("Любое количество именованных аргументов")


def any_kwargs(**kwargs):
    print(kwargs)


any_kwargs(test=1, money=2)

# Функция принимающая любое количество любых аргументов
# Первыми нужно передавать позиционные, потом именованные
print("Любое количество любых аргументов")


def any_of_any(*args, **kwargs):
    print(args)
    print(kwargs)


any_of_any(1, 2, 3, 4, test=1, money=2)


# Распаковка значений при передаче в функцию
print("Распаковка значений из списков")
l = [1, 2, 3, 4, 5]
d = {"key1": "value1", "key2": "value2"}


def foo_position(*args):
    print(args)


def foo_named(key1, key2):
    print(key1, key2)


foo_position(*l)
foo_named(**d)
