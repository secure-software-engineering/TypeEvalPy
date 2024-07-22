# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'aoyeg': 82, 'xzquc': 41, 'demfu': 10}


class MySubClass(MyClass):
    def func(self):
        return False


a = MySubClass()
b = a.func()
