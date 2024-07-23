# Method Overriding by imherited class
class MyClass:
    def func(self):
        return False


class MySubClass(MyClass):
    def func(self):
        return 'smloy'


a = MySubClass()
b = a.func()
