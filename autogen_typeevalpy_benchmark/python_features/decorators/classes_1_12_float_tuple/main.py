# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 50.3

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return (13, 69, 26)


a = MyClass()
b = a.my_method()
