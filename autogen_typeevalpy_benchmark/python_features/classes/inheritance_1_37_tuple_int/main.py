# Calling methods of inherited class
class MyClass:
    def func(self):
        return (52, 4, 82)


class MySubClass(MyClass):
    def sub_func(self):
        return 68


a = MySubClass()
b = a.func()
c = a.sub_func()
