# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (68, 82, 100)


class MySubClass(MyClass):
    def func(self):
        return False


a = MySubClass()
b = a.func()
