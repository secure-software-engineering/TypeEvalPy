# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [5, 56, 41]


class MySubClass(MyClass):
    def func(self):
        return {'ufwcb': 54, 'qfukb': 95, 'qizwj': 58}


a = MySubClass()
b = a.func()
