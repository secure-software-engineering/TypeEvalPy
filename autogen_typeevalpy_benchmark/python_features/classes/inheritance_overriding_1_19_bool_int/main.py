# Method Overriding by imherited class
class MyClass:
    def func(self):
        return False


class MySubClass(MyClass):
    def func(self):
        return 60


a = MySubClass()
b = a.func()
