# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'uykpz': 26, 'dlell': 19, 'lmzec': 81}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 'nuvmu'


a = MyClass()
b = a.my_method()
