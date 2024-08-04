# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'kmjmz'


class MySubClass(MyClass):
    def func(self):
        return 44.34


a = MySubClass()
b = a.func()
