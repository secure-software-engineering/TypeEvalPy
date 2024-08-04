# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return [61, 53, 90]

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return (80, 19, 100)


a = MyClass()
b = a.my_method()
