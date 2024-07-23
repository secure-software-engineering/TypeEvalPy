# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 95.68

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 92


a = MyClass()
b = a.my_method()
