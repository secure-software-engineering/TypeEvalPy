# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'tuhof': 74, 'asend': 83, 'scdqz': 41}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 19


a = MyClass()
b = a.my_method()
