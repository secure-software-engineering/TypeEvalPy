# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 'nsyma'

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'hwrmq': 17, 'ahwzq': 63, 'ytvbm': 84}


a = MyClass()
b = a.my_method()
