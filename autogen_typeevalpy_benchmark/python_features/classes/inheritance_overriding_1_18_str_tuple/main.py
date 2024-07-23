# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'mzind'


class MySubClass(MyClass):
    def func(self):
        return (90, 95, 13)


a = MySubClass()
b = a.func()
