# Calling methods of inherited class
class MyClass:
    def func(self):
        return (22, 97, 26)


class MySubClass(MyClass):
    def sub_func(self):
        return False


a = MySubClass()
b = a.func()
c = a.sub_func()
