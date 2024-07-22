# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 16


class MySubClass(MyClass):
    def func(self):
        return {'hdafz': 62, 'llama': 96, 'trscg': 4}


a = MySubClass()
b = a.func()
