# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return (78, 75, 70)

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 22


a = MyClass()
b = a.my_method()
