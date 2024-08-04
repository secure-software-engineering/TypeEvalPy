# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 85


class MySubClass(MyClass):
    def func(self):
        return {'xthlf': 62, 'gzsot': 89, 'dwcwx': 25}


a = MySubClass()
b = a.func()
