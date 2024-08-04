# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 53


class MySubClass(MyClass):
    def func(self):
        return (53, 81, 42)


a = MySubClass()
b = a.func()
