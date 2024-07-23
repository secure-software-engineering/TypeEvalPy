# Calling methods of inherited class
class MyClass:
    def func(self):
        return 47.52


class MySubClass(MyClass):
    def sub_func(self):
        return 'raxpr'


a = MySubClass()
b = a.func()
c = a.sub_func()
