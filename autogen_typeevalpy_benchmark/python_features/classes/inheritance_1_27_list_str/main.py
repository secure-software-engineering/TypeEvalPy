# Calling methods of inherited class
class MyClass:
    def func(self):
        return [75, 81, 37]


class MySubClass(MyClass):
    def sub_func(self):
        return 'afgjk'


a = MySubClass()
b = a.func()
c = a.sub_func()
