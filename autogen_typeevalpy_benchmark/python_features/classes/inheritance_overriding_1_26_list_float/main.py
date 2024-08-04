# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [15, 89, 53]


class MySubClass(MyClass):
    def func(self):
        return 97.81


a = MySubClass()
b = a.func()
