# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return [17, 99, 81]

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return (33, 40, 66)


a = MyClass()
b = a.my_method()
