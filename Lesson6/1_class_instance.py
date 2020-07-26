class Car:  # Объявление класса Car
    pass


class Animal:  # Объявление класса Animal
    pass


# Создание объектов (экземпляров) классов
toyota = Car()
lada = Car()
dog = Animal()

# Проверка на экземпляр класса
print("toyota <- Car", isinstance(toyota, Car))
print("lada <- Car", isinstance(lada, Car))
print("dog <- Car", isinstance(dog, Car))
print("dog is an Animal it's {}".format(object.__instancecheck__(dog)))
print(dog)
# Это не создание в присвоение
honda = Car
print(honda)
civic = honda()
print(isinstance(civic, Car))
