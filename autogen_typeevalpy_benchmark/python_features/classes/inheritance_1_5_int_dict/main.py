# Calling methods of inherited class
class MyClass:
    def func(self):
        return 85


class MySubClass(MyClass):
    def sub_func(self):
        return {'fdtgo': 1, 'igvex': 24, 'wshte': 65}


a = MySubClass()
b = a.func()
c = a.sub_func()
