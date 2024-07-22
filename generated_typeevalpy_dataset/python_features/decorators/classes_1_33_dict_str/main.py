# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'uqcwc': 26, 'zcpvy': 57, 'qyeyt': 21}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 'eeyfq'


a = MyClass()
b = a.my_method()
