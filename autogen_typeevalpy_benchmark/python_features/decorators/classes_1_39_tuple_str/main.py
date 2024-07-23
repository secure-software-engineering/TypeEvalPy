# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return (69, 63, 21)

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 'skhoo'


a = MyClass()
b = a.my_method()
