# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'chvdm': 25, 'phcqn': 56, 'voxkh': 39}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 21.55


a = MyClass()
b = a.my_method()
