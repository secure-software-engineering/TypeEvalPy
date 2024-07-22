# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return False

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'aowkr': 31, 'xoxzw': 82, 'gmhdz': 61}


a = MyClass()
b = a.my_method()
