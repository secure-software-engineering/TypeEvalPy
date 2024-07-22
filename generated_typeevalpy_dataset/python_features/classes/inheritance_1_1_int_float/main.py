# Calling methods of inherited class
class MyClass:
    def func(self):
        return 36


class MySubClass(MyClass):
    def sub_func(self):
        return 90.78


a = MySubClass()
b = a.func()
c = a.sub_func()
