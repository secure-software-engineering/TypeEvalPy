# Calling methods of inherited class
class MyClass:
    def func(self):
        return [16, 27, 45]


class MySubClass(MyClass):
    def sub_func(self):
        return 15.75


a = MySubClass()
b = a.func()
c = a.sub_func()
