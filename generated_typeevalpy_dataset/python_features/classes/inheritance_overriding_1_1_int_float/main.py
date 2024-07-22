# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 38


class MySubClass(MyClass):
    def func(self):
        return 33.72


a = MySubClass()
b = a.func()
