# Calling methods of inherited class
class MyClass:
    def func(self):
        return False


class MySubClass(MyClass):
    def sub_func(self):
        return 'tnvjs'


a = MySubClass()
b = a.func()
c = a.sub_func()
