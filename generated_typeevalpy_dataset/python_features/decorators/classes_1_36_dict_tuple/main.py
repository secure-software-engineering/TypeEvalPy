# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'xyold': 22, 'mbxao': 100, 'doghe': 33}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return (62, 73, 57)


a = MyClass()
b = a.my_method()
