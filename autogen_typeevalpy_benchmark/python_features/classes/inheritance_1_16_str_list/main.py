# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'tafak'


class MySubClass(MyClass):
    def sub_func(self):
        return [33, 13, 37]


a = MySubClass()
b = a.func()
c = a.sub_func()
