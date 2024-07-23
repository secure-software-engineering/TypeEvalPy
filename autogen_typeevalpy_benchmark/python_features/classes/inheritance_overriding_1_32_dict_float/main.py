# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'kclgy': 4, 'fwnxf': 63, 'deybe': 94}


class MySubClass(MyClass):
    def func(self):
        return 97.85


a = MySubClass()
b = a.func()
