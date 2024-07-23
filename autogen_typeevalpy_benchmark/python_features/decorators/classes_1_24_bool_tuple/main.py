# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return False

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return (3, 10, 56)


a = MyClass()
b = a.my_method()
