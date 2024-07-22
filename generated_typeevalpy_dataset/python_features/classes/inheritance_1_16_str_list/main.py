# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'txxsw'


class MySubClass(MyClass):
    def sub_func(self):
        return [29, 84, 90]


a = MySubClass()
b = a.func()
c = a.sub_func()
