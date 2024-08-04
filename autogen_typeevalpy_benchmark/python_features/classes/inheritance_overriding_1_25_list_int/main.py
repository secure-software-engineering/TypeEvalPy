# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [36, 21, 81]


class MySubClass(MyClass):
    def func(self):
        return 84


a = MySubClass()
b = a.func()
