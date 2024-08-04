# Method Overriding by imherited class
class MyClass:
    def func(self):
        return {'ryikd': 97, 'kiaje': 58, 'rbcuy': 89}


class MySubClass(MyClass):
    def func(self):
        return 95.26


a = MySubClass()
b = a.func()
