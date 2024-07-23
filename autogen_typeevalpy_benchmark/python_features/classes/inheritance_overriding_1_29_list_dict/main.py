# Method Overriding by imherited class
class MyClass:
    def func(self):
        return [27, 75, 53]


class MySubClass(MyClass):
    def func(self):
        return {'rvwyw': 17, 'nxexq': 46, 'tuwxs': 88}


a = MySubClass()
b = a.func()
