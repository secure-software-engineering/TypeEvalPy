# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (7, 44, 49)


class MySubClass(MyClass):
    def func(self):
        return 'zsiqs'


a = MySubClass()
b = a.func()
