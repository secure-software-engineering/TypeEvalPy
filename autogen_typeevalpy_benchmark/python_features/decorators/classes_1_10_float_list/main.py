# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 14.14

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return [47, 32, 49]


a = MyClass()
b = a.my_method()
