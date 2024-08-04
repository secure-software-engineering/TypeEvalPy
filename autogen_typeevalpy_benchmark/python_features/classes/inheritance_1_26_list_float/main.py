# Calling methods of inherited class
class MyClass:
    def func(self):
        return [46, 17, 69]


class MySubClass(MyClass):
    def sub_func(self):
        return 68.16


a = MySubClass()
b = a.func()
c = a.sub_func()
