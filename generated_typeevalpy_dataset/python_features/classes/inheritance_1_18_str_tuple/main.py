# Calling methods of inherited class
class MyClass:
    def func(self):
        return 'omblm'


class MySubClass(MyClass):
    def sub_func(self):
        return (54, 60, 23)


a = MySubClass()
b = a.func()
c = a.sub_func()
