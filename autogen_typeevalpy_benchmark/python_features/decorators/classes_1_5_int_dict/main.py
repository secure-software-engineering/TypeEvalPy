# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 98

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'ijsms': 78, 'ivvez': 91, 'xldqm': 70}


a = MyClass()
b = a.my_method()
