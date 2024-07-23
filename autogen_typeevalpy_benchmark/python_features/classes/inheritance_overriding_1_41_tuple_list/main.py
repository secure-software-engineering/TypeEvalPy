# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (91, 56, 24)


class MySubClass(MyClass):
    def func(self):
        return [43, 7, 53]


a = MySubClass()
b = a.func()
