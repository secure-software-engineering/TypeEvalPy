# Calling methods of inherited class
class MyClass:
    def func(self):
        return True


class MySubClass(MyClass):
    def sub_func(self):
        return (56, 67, 77)


a = MySubClass()
b = a.func()
c = a.sub_func()
