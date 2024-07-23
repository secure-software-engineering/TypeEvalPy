# Calling methods of inherited class
class MyClass:
    def func(self):
        return 67.99


class MySubClass(MyClass):
    def sub_func(self):
        return 75


a = MySubClass()
b = a.func()
c = a.sub_func()
