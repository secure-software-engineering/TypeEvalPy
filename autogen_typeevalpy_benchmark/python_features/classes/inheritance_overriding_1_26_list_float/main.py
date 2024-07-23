# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [54, 28, 48]


class MySubClass(MyClass):
    def func(self):
        return 99.31


a = MySubClass()
b = a.func()
