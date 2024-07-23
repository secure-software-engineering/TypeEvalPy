# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return (28, 52, 21)

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 90.24


a = MyClass()
b = a.my_method()
