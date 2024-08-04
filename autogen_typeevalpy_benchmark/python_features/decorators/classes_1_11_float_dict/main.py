# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 51.83

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'edbdi': 27, 'hboya': 84, 'palum': 72}


a = MyClass()
b = a.my_method()
