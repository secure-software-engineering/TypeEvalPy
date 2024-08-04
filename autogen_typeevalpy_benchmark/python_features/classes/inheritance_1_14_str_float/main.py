# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'htyzr'


class MySubClass(MyClass):
    def sub_func(self):
        return 23.96


a = MySubClass()
b = a.func()
c = a.sub_func()
