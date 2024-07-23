# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'bouhb': 68, 'ccwzj': 6, 'fqpae': 33}


class MySubClass(MyClass):
    def sub_func(self):
        return (15, 3, 35)


a = MySubClass()
b = a.func()
c = a.sub_func()
