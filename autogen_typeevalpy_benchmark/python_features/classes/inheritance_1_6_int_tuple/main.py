# Calling methods of inherited class
class MyClass:
    def func(self):
        return 86


class MySubClass(MyClass):
    def sub_func(self):
        return (71, 10, 46)


a = MySubClass()
b = a.func()
c = a.sub_func()
