# Calling methods of inherited class
class MyClass:
    def func(self):
        return (75, 33, 5)


class MySubClass(MyClass):
    def sub_func(self):
        return 97.21


a = MySubClass()
b = a.func()
c = a.sub_func()
