# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 'fiqzq'

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'edrzr': 85, 'uoixb': 82, 'eziyy': 23}


a = MyClass()
b = a.my_method()
