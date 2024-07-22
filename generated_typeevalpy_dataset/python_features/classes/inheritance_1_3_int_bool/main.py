# Calling methods of inherited class
class MyClass:
    def func(self):
        return 43


class MySubClass(MyClass):
    def sub_func(self):
        return True


a = MySubClass()
b = a.func()
c = a.sub_func()
