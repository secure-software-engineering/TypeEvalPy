# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return [100, 45, 2]

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 'sdzqr'


a = MyClass()
b = a.my_method()
