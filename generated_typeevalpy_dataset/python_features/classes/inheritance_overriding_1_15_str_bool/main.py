# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'wcbqk'


class MySubClass(MyClass):
    def func(self):
        return True


a = MySubClass()
b = a.func()
