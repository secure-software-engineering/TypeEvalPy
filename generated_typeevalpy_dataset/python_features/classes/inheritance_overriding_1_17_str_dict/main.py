# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'ragsy'


class MySubClass(MyClass):
    def func(self):
        return {'kmwsg': 44, 'jakmh': 99, 'ipucv': 18}


a = MySubClass()
b = a.func()
