# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 33.78


class MySubClass(MyClass):
    def func(self):
        return 'svpdh'


a = MySubClass()
b = a.func()
