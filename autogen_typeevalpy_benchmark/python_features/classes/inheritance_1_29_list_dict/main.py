# Calling methods of inherited class
class MyClass:
    def func(self):
        return [62, 57, 48]


class MySubClass(MyClass):
    def sub_func(self):
        return {'dxkho': 44, 'brcfm': 32, 'bigqb': 63}


a = MySubClass()
b = a.func()
c = a.sub_func()
