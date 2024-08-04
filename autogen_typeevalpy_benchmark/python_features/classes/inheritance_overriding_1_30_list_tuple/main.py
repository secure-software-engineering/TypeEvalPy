# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [16, 4, 57]


class MySubClass(MyClass):
    def func(self):
        return (2, 95, 45)


a = MySubClass()
b = a.func()
