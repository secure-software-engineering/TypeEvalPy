# Calling methods of inherited class
class MyClass:
    def func(self):
        return (38, 13, 93)


class MySubClass(MyClass):
    def sub_func(self):
        return 69.87


a = MySubClass()
b = a.func()
c = a.sub_func()
