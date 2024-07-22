# Calling methods of inherited class
class MyClass:
    def func(self):
        return (74, 62, 74)


class MySubClass(MyClass):
    def sub_func(self):
        return 'stpfw'


a = MySubClass()
b = a.func()
c = a.sub_func()
