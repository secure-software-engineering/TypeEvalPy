# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'leunj': 3, 'pzwyk': 47, 'dyfyc': 63}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 25.87


a = MyClass()
b = a.my_method()
