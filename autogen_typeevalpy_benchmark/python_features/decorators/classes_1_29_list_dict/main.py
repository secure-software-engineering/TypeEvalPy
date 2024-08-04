# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return [66, 4, 46]

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'tvcas': 28, 'vmqbh': 99, 'zblpv': 20}


a = MyClass()
b = a.my_method()
