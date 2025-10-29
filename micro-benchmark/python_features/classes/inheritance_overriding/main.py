# Method Overriding by imherited class
class MyClass:
    def func(self):
        return "Hello from func in MyClass"


class MySubClass(MyClass):
    def func(self):
        return 42

MyClass().func()
a = MySubClass()
b = a.func()
