# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'lfyaw'


class MySubClass(MyClass):
    def func(self):
        return [98, 38, 23]


a = MySubClass()
b = a.func()
