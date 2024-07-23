# Calling methods of inherited class
class MyClass:
    def func(self):
        return False


class MySubClass(MyClass):
    def sub_func(self):
        return [13, 2, 66]


a = MySubClass()
b = a.func()
c = a.sub_func()
