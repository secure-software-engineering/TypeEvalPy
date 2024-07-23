# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return [89, 2, 94]

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 'kddgf'


a = MyClass()
b = a.my_method()
