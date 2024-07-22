# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (54, 77, 61)


class MySubClass(MyClass):
    def func(self):
        return 29.76


a = MySubClass()
b = a.func()
