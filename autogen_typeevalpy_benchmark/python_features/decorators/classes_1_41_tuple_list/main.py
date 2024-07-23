# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return (45, 63, 94)

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return [20, 67, 53]


a = MyClass()
b = a.my_method()
