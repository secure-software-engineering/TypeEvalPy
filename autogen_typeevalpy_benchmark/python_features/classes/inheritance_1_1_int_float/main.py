# Calling methods of inherited class
class MyClass:
    def func(self):
        return 12


class MySubClass(MyClass):
    def sub_func(self):
        return 55.98


a = MySubClass()
b = a.func()
c = a.sub_func()
