# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [9, 78, 56]


class MySubClass(MyClass):
    def func(self):
        return 'qtbnu'


a = MySubClass()
b = a.func()
