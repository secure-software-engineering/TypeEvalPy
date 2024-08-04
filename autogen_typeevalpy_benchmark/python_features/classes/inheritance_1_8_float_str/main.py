# Calling methods of inherited class
class MyClass:
    def func(self):
        return 5.71


class MySubClass(MyClass):
    def sub_func(self):
        return 'pzjcl'


a = MySubClass()
b = a.func()
c = a.sub_func()
