# Calling methods of inherited class
class MyClass:
    def func(self):
        return [52, 83, 10]


class MySubClass(MyClass):
    def sub_func(self):
        return (47, 65, 63)


a = MySubClass()
b = a.func()
c = a.sub_func()
