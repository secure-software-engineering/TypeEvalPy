# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (82, 24, 14)


class MySubClass(MyClass):
    def func(self):
        return [100, 31, 9]


a = MySubClass()
b = a.func()
