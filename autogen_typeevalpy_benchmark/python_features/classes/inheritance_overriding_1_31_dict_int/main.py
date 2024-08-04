# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'rzaze': 90, 'yakmu': 70, 'hdeyp': 76}


class MySubClass(MyClass):
    def func(self):
        return 56


a = MySubClass()
b = a.func()
