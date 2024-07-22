# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (15, 95, 68)


class MySubClass(MyClass):
    def func(self):
        return 19


a = MySubClass()
b = a.func()
