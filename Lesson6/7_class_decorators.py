class Example:
    __counter = 0
    __hidden_attribute = "I'm hidden"

    def __init__(self):
        if self.__up_counter() > 4:
            raise Exception("Too many classes created!")

    @property
    def hidden(self):
        return self.__hidden_attribute + ", but accessible!"

    @staticmethod
    def static():
        print("Call this method without instance, its ok!")

    @classmethod
    def __up_counter(cls):
        cls.__counter += 1
        return cls.__counter

    @classmethod
    def instances_created(self):
        return self.__counter


Example.static()

ex = Example()
print(ex.hidden)

ex2 = Example()
ex3 = Example()

print(Example.instances_created())

ex4 = Example()

print(Example.instances_created())

ex5 = Example()
