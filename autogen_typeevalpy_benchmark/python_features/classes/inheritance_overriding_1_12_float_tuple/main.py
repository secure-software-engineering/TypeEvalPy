# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 26.46


class MySubClass(MyClass):
    def func(self):
        return (21, 45, 49)


a = MySubClass()
b = a.func()
