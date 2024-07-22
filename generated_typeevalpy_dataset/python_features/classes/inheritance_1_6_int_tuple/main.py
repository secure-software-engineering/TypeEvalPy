# Calling methods of inherited class
class MyClass:
    def func(self):
        return 35


class MySubClass(MyClass):
    def sub_func(self):
        return (27, 52, 8)


a = MySubClass()
b = a.func()
c = a.sub_func()
