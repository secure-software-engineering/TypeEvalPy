# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 81


class MySubClass(MyClass):
    def func(self):
        return 'qrhye'


a = MySubClass()
b = a.func()
