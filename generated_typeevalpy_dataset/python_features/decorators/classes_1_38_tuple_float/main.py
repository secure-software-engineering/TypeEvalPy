# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return (85, 81, 66)

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 45.23


a = MyClass()
b = a.my_method()
