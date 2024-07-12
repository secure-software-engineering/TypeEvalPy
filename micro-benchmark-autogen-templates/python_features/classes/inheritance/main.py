# Calling methods of inherited class
class MyClass:
    def func(self):
        return <value1>


class MySubClass(MyClass):
    def sub_func(self):
        return <value2>


a = MySubClass()
b = a.func()
c = a.sub_func()
