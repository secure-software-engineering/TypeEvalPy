# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return (76, 32, 97)

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return {'ljzlo': 45, 'wgdsf': 41, 'shszh': 37}


a = MyClass()
b = a.my_method()
