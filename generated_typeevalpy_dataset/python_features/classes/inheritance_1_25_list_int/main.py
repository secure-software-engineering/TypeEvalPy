# Calling methods of inherited class
class MyClass:
    def func(self):
        return [92, 87, 38]


class MySubClass(MyClass):
    def sub_func(self):
        return 72


a = MySubClass()
b = a.func()
c = a.sub_func()
