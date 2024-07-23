# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 14.62


class MySubClass(MyClass):
    def func(self):
        return (51, 94, 46)


a = MySubClass()
b = a.func()
