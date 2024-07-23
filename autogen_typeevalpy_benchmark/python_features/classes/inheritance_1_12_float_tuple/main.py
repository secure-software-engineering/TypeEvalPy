# Calling methods of inherited class
class MyClass:
    def func(self):
        return 88.25


class MySubClass(MyClass):
    def sub_func(self):
        return (52, 58, 86)


a = MySubClass()
b = a.func()
c = a.sub_func()
