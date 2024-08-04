# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 23


class MySubClass(MyClass):
    def func(self):
        return [94, 72, 65]


a = MySubClass()
b = a.func()
