# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return (65, 84, 84)

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'blyka': 21, 'uxwnx': 48, 'bxmbs': 22}


a = MyClass()
b = a.my_method()
