# Method Overriding by imherited class
class MyClass:
    def func(self):
        return False


class MySubClass(MyClass):
    def func(self):
        return 'zpahr'


a = MySubClass()
b = a.func()
