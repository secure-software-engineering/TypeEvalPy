# Method Overriding by imherited class
class MyClass:
    def func(self):
        return False


class MySubClass(MyClass):
    def func(self):
        return [95, 98, 60]


a = MySubClass()
b = a.func()
