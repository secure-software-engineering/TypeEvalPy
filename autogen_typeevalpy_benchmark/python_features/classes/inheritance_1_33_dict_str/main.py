# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'lbivk': 61, 'woygk': 27, 'uafra': 52}


class MySubClass(MyClass):
    def sub_func(self):
        return 'owpxn'


a = MySubClass()
b = a.func()
c = a.sub_func()
