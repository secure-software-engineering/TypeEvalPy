# Calling methods of inherited class
class MyClass:
    def func(self):
        return 68


class MySubClass(MyClass):
    def sub_func(self):
        return 'zkimh'


a = MySubClass()
b = a.func()
c = a.sub_func()