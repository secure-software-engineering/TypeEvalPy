# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'xeowz'


class MySubClass(MyClass):
    def func(self):
        return [82, 87, 31]


a = MySubClass()
b = a.func()
