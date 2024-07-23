# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 4.29

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'nqorz': 100, 'yrdev': 20, 'rlmzg': 82}


a = MyClass()
b = a.my_method()
