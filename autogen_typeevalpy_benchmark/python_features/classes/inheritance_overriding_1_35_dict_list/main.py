# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'ncplq': 83, 'nbvpz': 94, 'gluhr': 94}


class MySubClass(MyClass):
    def func(self):
        return [16, 18, 52]


a = MySubClass()
b = a.func()
