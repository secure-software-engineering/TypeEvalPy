# Calling methods of inherited class
class MyClass:
    def func(self):
        return [27, 65, 82]


class MySubClass(MyClass):
    def sub_func(self):
        return 20


a = MySubClass()
b = a.func()
c = a.sub_func()
