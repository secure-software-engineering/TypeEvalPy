# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'fxzbs': 27, 'zmeau': 87, 'igvug': 34}


class MySubClass(MyClass):
    def func(self):
        return [31, 99, 77]


a = MySubClass()
b = a.func()
