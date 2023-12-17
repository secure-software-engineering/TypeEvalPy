# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return "Hello from my_method in NewClass"

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 42


a = MyClass()
b = a.my_method()
