# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return [31, 67, 74]

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return (94, 58, 91)


a = MyClass()
b = a.my_method()
