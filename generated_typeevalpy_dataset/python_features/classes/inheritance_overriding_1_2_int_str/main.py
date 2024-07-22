# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 100


class MySubClass(MyClass):
    def func(self):
        return 'zhenp'


a = MySubClass()
b = a.func()
