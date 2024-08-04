# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'lrfrx': 14, 'zspuj': 38, 'ktjtp': 49}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 'suycl'


a = MyClass()
b = a.my_method()
