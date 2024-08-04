# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 84.11


class MySubClass(MyClass):
    def func(self):
        return {'iztdq': 29, 'pusmd': 90, 'isaqm': 3}


a = MySubClass()
b = a.func()
