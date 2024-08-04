# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (95, 15, 89)


class MySubClass(MyClass):
    def func(self):
        return 72.45


a = MySubClass()
b = a.func()
