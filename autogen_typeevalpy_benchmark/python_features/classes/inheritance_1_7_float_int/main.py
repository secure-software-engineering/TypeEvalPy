# Calling methods of inherited class
class MyClass:
    def func(self):
        return 78.83


class MySubClass(MyClass):
    def sub_func(self):
        return 24


a = MySubClass()
b = a.func()
c = a.sub_func()
