# Calling methods of inherited class
class MyClass:
    def func(self):
        return False


class MySubClass(MyClass):
    def sub_func(self):
        return {'tmupk': 14, 'ylfjb': 70, 'hwmca': 1}


a = MySubClass()
b = a.func()
c = a.sub_func()
