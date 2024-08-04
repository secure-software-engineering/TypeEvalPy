# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'kdzon'


class MySubClass(MyClass):
    def sub_func(self):
        return 37


a = MySubClass()
b = a.func()
c = a.sub_func()
