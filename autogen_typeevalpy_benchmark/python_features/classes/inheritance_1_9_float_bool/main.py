# Calling methods of inherited class
class MyClass:
    def func(self):
        return 99.58


class MySubClass(MyClass):
    def sub_func(self):
        return False


a = MySubClass()
b = a.func()
c = a.sub_func()
