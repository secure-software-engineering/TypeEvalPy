# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'gyxai'


class MySubClass(MyClass):
    def func(self):
        return 74


a = MySubClass()
b = a.func()
