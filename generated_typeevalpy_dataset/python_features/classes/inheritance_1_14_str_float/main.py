# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'dyylp'


class MySubClass(MyClass):
    def sub_func(self):
        return 39.62


a = MySubClass()
b = a.func()
c = a.sub_func()
