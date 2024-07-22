# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 'iafpx'

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return [87, 28, 44]


a = MyClass()
b = a.my_method()
