# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return [99, 85, 73]

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return False


a = MyClass()
b = a.my_method()
