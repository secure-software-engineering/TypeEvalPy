# Calling methods of inherited class
class MyClass:
    def func(self):
        return 58


class MySubClass(MyClass):
    def sub_func(self):
        return [19, 69, 4]


a = MySubClass()
b = a.func()
c = a.sub_func()
