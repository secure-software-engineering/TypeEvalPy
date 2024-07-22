# Method Overriding by imherited class
class MyClass:
    def func(self):
        return True


class MySubClass(MyClass):
    def func(self):
        return 96


a = MySubClass()
b = a.func()
