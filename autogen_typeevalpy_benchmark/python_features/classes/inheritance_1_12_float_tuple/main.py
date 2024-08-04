# Calling methods of inherited class
class MyClass:
    def func(self):
        return 75.81


class MySubClass(MyClass):
    def sub_func(self):
        return (63, 33, 77)


a = MySubClass()
b = a.func()
c = a.sub_func()
