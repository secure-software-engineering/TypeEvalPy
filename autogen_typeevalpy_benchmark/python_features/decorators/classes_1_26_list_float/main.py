# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return [71, 66, 61]

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 67.58


a = MyClass()
b = a.my_method()
