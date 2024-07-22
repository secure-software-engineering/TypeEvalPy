# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'pituy': 82, 'futlq': 21, 'twavs': 44}


class MySubClass(MyClass):
    def func(self):
        return 47.93


a = MySubClass()
b = a.func()
