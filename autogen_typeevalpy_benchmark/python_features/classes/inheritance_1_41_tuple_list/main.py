# Calling methods of inherited class
class MyClass:
    def func(self):
        return (27, 16, 68)


class MySubClass(MyClass):
    def sub_func(self):
        return [42, 48, 73]


a = MySubClass()
b = a.func()
c = a.sub_func()
