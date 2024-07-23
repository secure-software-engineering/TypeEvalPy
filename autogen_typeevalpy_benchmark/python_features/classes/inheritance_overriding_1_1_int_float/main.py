# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 39


class MySubClass(MyClass):
    def func(self):
        return 53.18


a = MySubClass()
b = a.func()
