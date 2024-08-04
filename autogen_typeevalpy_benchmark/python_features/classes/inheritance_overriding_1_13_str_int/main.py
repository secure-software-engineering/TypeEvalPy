# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'ybhfc'


class MySubClass(MyClass):
    def func(self):
        return 88


a = MySubClass()
b = a.func()
