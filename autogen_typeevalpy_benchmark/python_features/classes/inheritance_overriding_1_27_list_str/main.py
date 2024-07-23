# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [74, 81, 46]


class MySubClass(MyClass):
    def func(self):
        return 'ympzs'


a = MySubClass()
b = a.func()
