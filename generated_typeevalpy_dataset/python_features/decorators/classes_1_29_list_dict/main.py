# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return [85, 99, 97]

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'vyfal': 47, 'eytxh': 10, 'imkqn': 13}


a = MyClass()
b = a.my_method()
