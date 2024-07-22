# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 77


class MySubClass(MyClass):
    def func(self):
        return (28, 75, 57)


a = MySubClass()
b = a.func()
