# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (93, 20, 20)


class MySubClass(MyClass):
    def func(self):
        return 'vyimt'


a = MySubClass()
b = a.func()
