# Method Overriding by imherited class
class MyClass:
    def func(self):
        return True


class MySubClass(MyClass):
    def func(self):
        return {'wefuv': 27, 'qivly': 86, 'cfoih': 90}


a = MySubClass()
b = a.func()
