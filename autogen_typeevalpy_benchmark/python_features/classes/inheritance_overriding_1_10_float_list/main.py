# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 71.04


class MySubClass(MyClass):
    def func(self):
        return [77, 83, 94]


a = MySubClass()
b = a.func()
