# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [71, 30, 14]


class MySubClass(MyClass):
    def func(self):
        return 30


a = MySubClass()
b = a.func()
