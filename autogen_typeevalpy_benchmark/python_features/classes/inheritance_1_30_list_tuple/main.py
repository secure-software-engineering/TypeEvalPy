# Calling methods of inherited class
class MyClass:
    def func(self):
        return [50, 35, 21]


class MySubClass(MyClass):
    def sub_func(self):
        return (79, 66, 30)


a = MySubClass()
b = a.func()
c = a.sub_func()
