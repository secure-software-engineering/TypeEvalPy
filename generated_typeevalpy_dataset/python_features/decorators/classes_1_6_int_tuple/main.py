# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 38

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return (57, 21, 98)


a = MyClass()
b = a.my_method()
