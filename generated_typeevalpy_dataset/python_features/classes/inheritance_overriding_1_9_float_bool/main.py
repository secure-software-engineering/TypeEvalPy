# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 76.8


class MySubClass(MyClass):
    def func(self):
        return False


a = MySubClass()
b = a.func()
