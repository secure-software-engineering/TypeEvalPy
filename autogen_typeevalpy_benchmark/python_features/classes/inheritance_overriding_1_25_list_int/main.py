# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [25, 50, 50]


class MySubClass(MyClass):
    def func(self):
        return 18


a = MySubClass()
b = a.func()
