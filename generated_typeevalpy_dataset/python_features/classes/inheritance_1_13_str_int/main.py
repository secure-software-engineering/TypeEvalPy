# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'vzsix'


class MySubClass(MyClass):
    def sub_func(self):
        return 33


a = MySubClass()
b = a.func()
c = a.sub_func()
