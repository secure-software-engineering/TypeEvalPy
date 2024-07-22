# Returning a custom object from a function.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def func():
    return Person("Alice", 25)


p = func()
