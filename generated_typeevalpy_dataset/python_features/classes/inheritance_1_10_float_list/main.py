# Calling methods of inherited class
class MyClass:
    def func(self):
        return 82.57


class MySubClass(MyClass):
    def sub_func(self):
        return [4, 78, 31]


a = MySubClass()
b = a.func()
c = a.sub_func()
