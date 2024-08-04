# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 99.19


class MySubClass(MyClass):
    def func(self):
        return 58


a = MySubClass()
b = a.func()
