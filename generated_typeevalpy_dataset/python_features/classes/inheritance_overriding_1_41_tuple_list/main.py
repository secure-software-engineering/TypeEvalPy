# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (25, 66, 14)


class MySubClass(MyClass):
    def func(self):
        return [46, 15, 98]


a = MySubClass()
b = a.func()
