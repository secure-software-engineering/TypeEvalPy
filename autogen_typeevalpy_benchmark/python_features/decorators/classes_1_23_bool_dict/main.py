# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return True

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'dcgmx': 32, 'gcnrz': 71, 'tjnxt': 81}


a = MyClass()
b = a.my_method()
