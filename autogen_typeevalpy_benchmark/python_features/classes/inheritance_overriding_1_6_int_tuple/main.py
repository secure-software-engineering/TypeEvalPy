# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 65


class MySubClass(MyClass):
    def func(self):
        return (44, 91, 75)


a = MySubClass()
b = a.func()
