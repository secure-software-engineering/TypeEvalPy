# Calling methods of inherited class
class MyClass:
    def func(self):
        return 39.86


class MySubClass(MyClass):
    def sub_func(self):
        return True


a = MySubClass()
b = a.func()
c = a.sub_func()
