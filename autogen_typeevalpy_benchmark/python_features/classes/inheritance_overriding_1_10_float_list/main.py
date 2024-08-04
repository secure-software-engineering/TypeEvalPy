# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 95.52


class MySubClass(MyClass):
    def func(self):
        return [62, 9, 8]


a = MySubClass()
b = a.func()
