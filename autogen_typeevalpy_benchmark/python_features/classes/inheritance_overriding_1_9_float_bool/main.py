# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 73.86


class MySubClass(MyClass):
    def func(self):
        return False


a = MySubClass()
b = a.func()
