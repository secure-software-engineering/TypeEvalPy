# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'fmrfo'


class MySubClass(MyClass):
    def func(self):
        return [32, 100, 47]


a = MySubClass()
b = a.func()
