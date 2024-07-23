# Calling methods of inherited class
class MyClass:
    def func(self):
        return 78


class MySubClass(MyClass):
    def sub_func(self):
        return 'ldyws'


a = MySubClass()
b = a.func()
c = a.sub_func()
