# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'rkbds': 55, 'rsxvc': 35, 'cofvx': 3}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return [82, 86, 60]


a = MyClass()
b = a.my_method()
