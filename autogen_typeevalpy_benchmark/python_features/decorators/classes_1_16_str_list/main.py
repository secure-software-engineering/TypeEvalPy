# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 'jqkxm'

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return [3, 6, 95]


a = MyClass()
b = a.my_method()
