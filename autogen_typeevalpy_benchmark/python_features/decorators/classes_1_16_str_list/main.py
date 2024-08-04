# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 'hbsiq'

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return [54, 1, 91]


a = MyClass()
b = a.my_method()
