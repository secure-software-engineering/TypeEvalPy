# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'ikcob': 61, 'zmyfq': 1, 'bontw': 10}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return [98, 2, 62]


a = MyClass()
b = a.my_method()
