# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'umhvs'


class MySubClass(MyClass):
    def func(self):
        return 33.63


a = MySubClass()
b = a.func()
