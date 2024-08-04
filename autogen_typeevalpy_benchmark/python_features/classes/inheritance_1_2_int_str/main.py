# Calling methods of inherited class
class MyClass:
    def func(self):
        return 4


class MySubClass(MyClass):
    def sub_func(self):
        return 'zqtvl'


a = MySubClass()
b = a.func()
c = a.sub_func()
