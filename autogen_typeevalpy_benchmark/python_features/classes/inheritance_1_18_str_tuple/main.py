# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'pwkga'


class MySubClass(MyClass):
    def sub_func(self):
        return (8, 1, 57)


a = MySubClass()
b = a.func()
c = a.sub_func()
