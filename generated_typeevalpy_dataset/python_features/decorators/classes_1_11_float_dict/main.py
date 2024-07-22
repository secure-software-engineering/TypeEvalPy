# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 22.4

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'ggmkx': 84, 'rmirt': 66, 'keooq': 63}


a = MyClass()
b = a.my_method()
