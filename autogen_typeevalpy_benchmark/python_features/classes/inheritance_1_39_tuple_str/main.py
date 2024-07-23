# Calling methods of inherited class
class MyClass:
    def func(self):
        return (38, 53, 74)


class MySubClass(MyClass):
    def sub_func(self):
        return 'axevd'


a = MySubClass()
b = a.func()
c = a.sub_func()
