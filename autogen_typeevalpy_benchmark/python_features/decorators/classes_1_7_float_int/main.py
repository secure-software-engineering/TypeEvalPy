# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 98.27

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 52


a = MyClass()
b = a.my_method()
