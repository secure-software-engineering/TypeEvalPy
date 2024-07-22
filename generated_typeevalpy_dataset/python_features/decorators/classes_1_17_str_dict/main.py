# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 'yszqa'

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'pzpah': 58, 'ocugu': 86, 'eccfg': 95}


a = MyClass()
b = a.my_method()
