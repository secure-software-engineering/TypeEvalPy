# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (85, 56, 76)


class MySubClass(MyClass):
    def func(self):
        return True


a = MySubClass()
b = a.func()
