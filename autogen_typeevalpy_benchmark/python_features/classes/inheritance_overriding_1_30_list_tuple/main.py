# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [68, 81, 72]


class MySubClass(MyClass):
    def func(self):
        return (10, 38, 2)


a = MySubClass()
b = a.func()
