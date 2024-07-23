# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 21


class MySubClass(MyClass):
    def func(self):
        return {'jvffa': 62, 'qiwok': 52, 'nrcgn': 98}


a = MySubClass()
b = a.func()
