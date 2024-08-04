# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return (88, 60, 47)

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 'cskco'


a = MyClass()
b = a.my_method()
