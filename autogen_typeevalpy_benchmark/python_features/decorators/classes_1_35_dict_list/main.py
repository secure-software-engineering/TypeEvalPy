# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'tipsd': 64, 'aaugv': 84, 'xylhb': 20}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return [50, 6, 95]


a = MyClass()
b = a.my_method()
