# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 44


class MySubClass(MyClass):
    def func(self):
        return [12, 42, 46]


a = MySubClass()
b = a.func()
