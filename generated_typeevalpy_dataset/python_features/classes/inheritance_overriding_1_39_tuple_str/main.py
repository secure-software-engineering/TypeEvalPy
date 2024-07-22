# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (84, 45, 8)


class MySubClass(MyClass):
    def func(self):
        return 'cvhui'


a = MySubClass()
b = a.func()
