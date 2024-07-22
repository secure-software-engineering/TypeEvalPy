# Calling methods of inherited class
class MyClass:
    def func(self):
        return 22


class MySubClass(MyClass):
    def sub_func(self):
        return [80, 25, 3]


a = MySubClass()
b = a.func()
c = a.sub_func()
