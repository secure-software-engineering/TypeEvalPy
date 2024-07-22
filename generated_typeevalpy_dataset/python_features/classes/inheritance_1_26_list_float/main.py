# Calling methods of inherited class
class MyClass:
    def func(self):
        return [90, 32, 89]


class MySubClass(MyClass):
    def sub_func(self):
        return 99.83


a = MySubClass()
b = a.func()
c = a.sub_func()
