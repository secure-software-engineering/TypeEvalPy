# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 69


class MySubClass(MyClass):
    def func(self):
        return [77, 65, 1]


a = MySubClass()
b = a.func()
