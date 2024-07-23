# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'mdixf'


class MySubClass(MyClass):
    def sub_func(self):
        return 51.75


a = MySubClass()
b = a.func()
c = a.sub_func()
