# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 56.79

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return [5, 25, 61]


a = MyClass()
b = a.my_method()
