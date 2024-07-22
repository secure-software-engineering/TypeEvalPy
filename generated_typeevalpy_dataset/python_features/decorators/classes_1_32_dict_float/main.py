# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'ipmyr': 59, 'rvtbv': 4, 'awzww': 84}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 39.81


a = MyClass()
b = a.my_method()
