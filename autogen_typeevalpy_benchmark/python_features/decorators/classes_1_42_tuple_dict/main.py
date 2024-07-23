# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return (56, 50, 97)

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'ubxhq': 71, 'zydry': 30, 'tvqxi': 82}


a = MyClass()
b = a.my_method()
