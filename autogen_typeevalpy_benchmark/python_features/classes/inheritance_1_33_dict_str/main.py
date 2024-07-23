# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'tnhya': 41, 'xfrde': 70, 'hhjib': 34}


class MySubClass(MyClass):
    def sub_func(self):
        return 'rgtcx'


a = MySubClass()
b = a.func()
c = a.sub_func()
