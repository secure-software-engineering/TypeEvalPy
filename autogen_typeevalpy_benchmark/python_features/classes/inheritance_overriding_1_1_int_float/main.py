# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 7


class MySubClass(MyClass):
    def func(self):
        return 72.93


a = MySubClass()
b = a.func()
