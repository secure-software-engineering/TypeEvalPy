# Calling methods of inherited class
class MyClass:
    def func(self):
        return 70


class MySubClass(MyClass):
    def sub_func(self):
        return [44, 30, 29]


a = MySubClass()
b = a.func()
c = a.sub_func()
