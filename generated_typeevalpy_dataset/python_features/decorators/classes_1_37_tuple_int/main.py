# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return (94, 57, 92)

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 99


a = MyClass()
b = a.my_method()
