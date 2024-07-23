# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return [85, 32, 14]

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'kfgye': 75, 'rbrpi': 96, 'pbchp': 74}


a = MyClass()
b = a.my_method()
