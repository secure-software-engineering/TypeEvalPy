# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 88.58


class MySubClass(MyClass):
    def func(self):
        return (26, 71, 92)


a = MySubClass()
b = a.func()
