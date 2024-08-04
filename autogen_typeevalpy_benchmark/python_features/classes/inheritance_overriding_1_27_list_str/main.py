# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [36, 29, 43]


class MySubClass(MyClass):
    def func(self):
        return 'feztx'


a = MySubClass()
b = a.func()
