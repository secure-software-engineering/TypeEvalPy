# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 1.09

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 'hsrmp'


a = MyClass()
b = a.my_method()
