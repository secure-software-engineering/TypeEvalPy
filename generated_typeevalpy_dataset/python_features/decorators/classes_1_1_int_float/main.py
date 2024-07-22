# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 83

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 91.3


a = MyClass()
b = a.my_method()
