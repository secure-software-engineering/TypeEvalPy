# Calling methods of inherited class
class MyClass:
    def func(self):
        return 85


class MySubClass(MyClass):
    def sub_func(self):
        return (86, 98, 90)


a = MySubClass()
b = a.func()
c = a.sub_func()
