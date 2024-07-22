# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [4, 48, 83]


class MySubClass(MyClass):
    def func(self):
        return 47.05


a = MySubClass()
b = a.func()
