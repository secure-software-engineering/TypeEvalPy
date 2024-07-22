# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'laylv'


class MySubClass(MyClass):
    def func(self):
        return 16.34


a = MySubClass()
b = a.func()
