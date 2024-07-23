# Calling methods of inherited class
class MyClass:
    def func(self):
        return [89, 9, 68]


class MySubClass(MyClass):
    def sub_func(self):
        return (59, 46, 85)


a = MySubClass()
b = a.func()
c = a.sub_func()
