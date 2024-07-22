# Calling methods of inherited class
class MyClass:
    def func(self):
        return (34, 58, 69)


class MySubClass(MyClass):
    def sub_func(self):
        return 95


a = MySubClass()
b = a.func()
c = a.sub_func()
