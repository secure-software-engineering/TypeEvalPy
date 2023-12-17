# Method Overriding by imherited class
class MyClass:
    def func(self):
        return "Hello from func in MyClass"


class MySubClass(MyClass):
    def func(self):
        return 42


a = MySubClass()
b = a.func()
