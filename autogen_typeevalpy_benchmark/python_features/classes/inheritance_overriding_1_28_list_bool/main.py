# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [100, 48, 32]


class MySubClass(MyClass):
    def func(self):
        return False


a = MySubClass()
b = a.func()
