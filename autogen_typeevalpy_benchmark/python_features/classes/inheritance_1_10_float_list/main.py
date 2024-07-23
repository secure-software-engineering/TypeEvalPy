# Calling methods of inherited class
class MyClass:
    def func(self):
        return 41.85


class MySubClass(MyClass):
    def sub_func(self):
        return [79, 6, 24]


a = MySubClass()
b = a.func()
c = a.sub_func()
