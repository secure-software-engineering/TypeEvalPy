# Calling methods of inherited class
class MyClass:
    def func(self):
        return (29, 48, 75)


class MySubClass(MyClass):
    def sub_func(self):
        return 18


a = MySubClass()
b = a.func()
c = a.sub_func()
