# Method Overriding by imherited class
class MyClass:
    def func(self):
        return 97.82


class MySubClass(MyClass):
    def func(self):
        return {'avdqa': 42, 'ynaqk': 8, 'kpiif': 15}


a = MySubClass()
b = a.func()
