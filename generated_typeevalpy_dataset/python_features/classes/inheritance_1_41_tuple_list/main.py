# Calling methods of inherited class
class MyClass:
    def func(self):
        return (1, 18, 65)


class MySubClass(MyClass):
    def sub_func(self):
        return [25, 39, 59]


a = MySubClass()
b = a.func()
c = a.sub_func()
