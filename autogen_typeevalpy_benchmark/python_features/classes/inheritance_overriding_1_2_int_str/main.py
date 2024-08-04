# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 40


class MySubClass(MyClass):
    def func(self):
        return 'zbtpe'


a = MySubClass()
b = a.func()
