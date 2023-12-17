# Calling methods of inherited class
class MyClass:
    def func(self):
        return "Hello from func in MyClass"


class MySubClass(MyClass):
    def sub_func(self):
        return 42


a = MySubClass()
b = a.func()
c = a.sub_func()
