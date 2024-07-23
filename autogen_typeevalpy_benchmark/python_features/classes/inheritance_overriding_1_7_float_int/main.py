# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 68.82


class MySubClass(MyClass):
    def func(self):
        return 36


a = MySubClass()
b = a.func()
