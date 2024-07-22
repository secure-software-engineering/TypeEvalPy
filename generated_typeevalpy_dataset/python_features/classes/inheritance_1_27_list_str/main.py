# Calling methods of inherited class
class MyClass:
    def func(self):
        return [26, 96, 28]


class MySubClass(MyClass):
    def sub_func(self):
        return 'nvlnj'


a = MySubClass()
b = a.func()
c = a.sub_func()
