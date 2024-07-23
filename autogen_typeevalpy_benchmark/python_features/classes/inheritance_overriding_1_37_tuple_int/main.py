# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (51, 1, 34)


class MySubClass(MyClass):
    def func(self):
        return 66


a = MySubClass()
b = a.func()
