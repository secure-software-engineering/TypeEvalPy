# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 74.47


class MySubClass(MyClass):
    def func(self):
        return 'yzsjj'


a = MySubClass()
b = a.func()
