# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 9

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'wwebq': 49, 'slfji': 97, 'jwcdl': 10}


a = MyClass()
b = a.my_method()
