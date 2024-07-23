# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return {'xqgar': 30, 'jwrel': 8, 'pjgjn': 39}

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return (30, 30, 92)


a = MyClass()
b = a.my_method()
