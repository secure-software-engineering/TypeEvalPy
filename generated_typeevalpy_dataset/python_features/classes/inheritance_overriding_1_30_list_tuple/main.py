# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [41, 40, 4]


class MySubClass(MyClass):
    def func(self):
        return (66, 1, 51)


a = MySubClass()
b = a.func()
