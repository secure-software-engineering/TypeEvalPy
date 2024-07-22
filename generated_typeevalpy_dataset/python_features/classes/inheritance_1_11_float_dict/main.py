# Calling methods of inherited class
class MyClass:
    def func(self):
        return 23.49


class MySubClass(MyClass):
    def sub_func(self):
        return {'shbav': 93, 'xsxdz': 16, 'tusls': 53}


a = MySubClass()
b = a.func()
c = a.sub_func()
