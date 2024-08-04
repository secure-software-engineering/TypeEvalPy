# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'eitpy': 25, 'fnjzm': 6, 'nvuzd': 73}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return (59, 4, 12)


a = MyClass()
b = a.my_method()
