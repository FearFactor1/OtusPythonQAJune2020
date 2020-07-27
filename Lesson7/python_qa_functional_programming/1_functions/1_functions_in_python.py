import inspect

print("Функци является объектом")


def hello_function(b):
    a = 1


# print(dir(hello_function))
# print("name:", hello_function.__name__)
# print("code:", hello_function.__code__)
# print("type:", type(hello_function))
# print(inspect.getsource(hello_function))

print("Возвращаемые значения из функций")
def fun(n=None):
    print('_function_' + str(n))


def fun_return():
    return '_function_'


# print(fun())
# print(fun_return())

print("Можем использовать функцию как любой другой объект")

list_of_functions = [fun, fun, fun]

# print(list_of_functions)

for function in list_of_functions:
    function(1)

print("Присваиваем функцию переменной")
another_name = fun
another_name()


print("Возвращаем функцию из функции")
def foo(f): return f
foo(fun)()


print("Функция без имени - lambda")
lambda_function = lambda x: x ** 2
lambda_function(10)
result = (lambda x: x ** 2)(10)
print(result)
