# Calling methods of inherited class
class MyClass:
    def func(self):
        return [67, 44, 69]


class MySubClass(MyClass):
    def sub_func(self):
        return 'ixmjk'


a = MySubClass()
b = a.func()
c = a.sub_func()
