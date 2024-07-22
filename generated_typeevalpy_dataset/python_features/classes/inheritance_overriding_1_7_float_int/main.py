# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 30.74


class MySubClass(MyClass):
    def func(self):
        return 19


a = MySubClass()
b = a.func()
