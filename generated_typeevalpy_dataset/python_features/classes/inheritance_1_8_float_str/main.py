# Calling methods of inherited class
class MyClass:
    def func(self):
        return 20.15


class MySubClass(MyClass):
    def sub_func(self):
        return 'zggsa'


a = MySubClass()
b = a.func()
c = a.sub_func()
