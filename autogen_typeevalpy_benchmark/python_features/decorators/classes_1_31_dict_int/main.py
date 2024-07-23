# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'ysxzc': 39, 'vebji': 100, 'uiwxa': 66}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 28


a = MyClass()
b = a.my_method()
