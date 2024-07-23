# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'ywnpz'


class MySubClass(MyClass):
    def func(self):
        return True


a = MySubClass()
b = a.func()
