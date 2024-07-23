# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (1, 23, 11)


class MySubClass(MyClass):
    def func(self):
        return 80.68


a = MySubClass()
b = a.func()
