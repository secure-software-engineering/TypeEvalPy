# Calling methods of inherited class
class MyClass:
    def func(self):
        return (87, 72, 100)


class MySubClass(MyClass):
    def sub_func(self):
        return 'ijmfs'


a = MySubClass()
b = a.func()
c = a.sub_func()
