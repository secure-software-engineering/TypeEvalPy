# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'odmkz'


class MySubClass(MyClass):
    def sub_func(self):
        return 45


a = MySubClass()
b = a.func()
c = a.sub_func()
