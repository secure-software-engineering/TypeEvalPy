# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (4, 44, 5)


class MySubClass(MyClass):
    def func(self):
        return 71


a = MySubClass()
b = a.func()
