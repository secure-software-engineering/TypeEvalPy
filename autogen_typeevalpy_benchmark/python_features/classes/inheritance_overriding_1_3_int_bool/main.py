# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 53


class MySubClass(MyClass):
    def func(self):
        return True


a = MySubClass()
b = a.func()
