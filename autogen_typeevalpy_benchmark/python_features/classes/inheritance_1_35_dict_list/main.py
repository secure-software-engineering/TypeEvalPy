# Calling methods of inherited class
class MyClass:
    def func(self):
        return {'urlyp': 92, 'kneki': 54, 'baniz': 58}


class MySubClass(MyClass):
    def sub_func(self):
        return [15, 19, 50]


a = MySubClass()
b = a.func()
c = a.sub_func()
