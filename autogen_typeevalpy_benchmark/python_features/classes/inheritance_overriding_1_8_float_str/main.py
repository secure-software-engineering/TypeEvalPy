# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 73.54


class MySubClass(MyClass):
    def func(self):
        return 'jxloz'


a = MySubClass()
b = a.func()
