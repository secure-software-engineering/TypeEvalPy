# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'mhmro'


class MySubClass(MyClass):
    def sub_func(self):
        return (89, 10, 61)


a = MySubClass()
b = a.func()
c = a.sub_func()
