# Method Overriding by imherited class
class MyClass:
    def func(self):
        return (13, 53, 90)


class MySubClass(MyClass):
    def func(self):
        return {'khadq': 94, 'eyhll': 45, 'kgndr': 73}


a = MySubClass()
b = a.func()
