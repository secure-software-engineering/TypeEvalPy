# Calling methods of inherited class
class MyClass:
    def func(self):
        return 75.92


class MySubClass(MyClass):
    def sub_func(self):
        return {'semqq': 6, 'whhku': 8, 'zxbma': 31}


a = MySubClass()
b = a.func()
c = a.sub_func()
