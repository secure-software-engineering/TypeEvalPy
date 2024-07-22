# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'mkkut': 98, 'wjfcr': 59, 'gxvsy': 99}


class MySubClass(MyClass):
    def sub_func(self):
        return 3.63


a = MySubClass()
b = a.func()
c = a.sub_func()
