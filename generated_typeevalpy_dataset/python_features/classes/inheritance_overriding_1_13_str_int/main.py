# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'iuqrk'


class MySubClass(MyClass):
    def func(self):
        return 21


a = MySubClass()
b = a.func()
