# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 'fsgat'


class MySubClass(MyClass):
    def func(self):
        return (45, 3, 80)


a = MySubClass()
b = a.func()
