# Calling methods of inherited class
class MyClass:
    def func(self):
        return (53, 84, 17)


class MySubClass(MyClass):
    def sub_func(self):
        return 39.76


a = MySubClass()
b = a.func()
c = a.sub_func()
