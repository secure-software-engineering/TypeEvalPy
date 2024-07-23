# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 4

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 'nedks'


a = MyClass()
b = a.my_method()
