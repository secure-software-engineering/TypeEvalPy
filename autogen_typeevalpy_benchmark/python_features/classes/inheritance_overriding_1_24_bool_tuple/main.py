# Method Overriding by imherited class
class MyClass:
    def func(self):
        return True


class MySubClass(MyClass):
    def func(self):
        return (75, 94, 39)


a = MySubClass()
b = a.func()
