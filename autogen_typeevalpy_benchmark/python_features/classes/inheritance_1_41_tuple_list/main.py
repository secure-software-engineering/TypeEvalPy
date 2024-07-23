# Calling methods of inherited class
class MyClass:
    def func(self):
        return (76, 97, 35)


class MySubClass(MyClass):
    def sub_func(self):
        return [52, 15, 58]


a = MySubClass()
b = a.func()
c = a.sub_func()
