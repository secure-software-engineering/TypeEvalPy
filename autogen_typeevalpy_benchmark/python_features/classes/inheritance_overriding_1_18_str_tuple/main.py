# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'iikxd'


class MySubClass(MyClass):
    def func(self):
        return (54, 7, 37)


a = MySubClass()
b = a.func()
