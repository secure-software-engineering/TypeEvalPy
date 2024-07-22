# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return (46, 78, 51)

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return [55, 37, 57]


a = MyClass()
b = a.my_method()
