# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 90.33


class MySubClass(MyClass):
    def func(self):
        return [60, 39, 16]


a = MySubClass()
b = a.func()
