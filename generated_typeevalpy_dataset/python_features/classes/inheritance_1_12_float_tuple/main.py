# Calling methods of inherited class
class MyClass:
    def func(self):
        return 6.48


class MySubClass(MyClass):
    def sub_func(self):
        return (93, 47, 42)


a = MySubClass()
b = a.func()
c = a.sub_func()
