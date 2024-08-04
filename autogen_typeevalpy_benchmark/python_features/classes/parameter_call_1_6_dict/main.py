# A class method is assigned parameters which are called.
class MyClass:
    def func3(self):
        return {'knain': 68, 'oiznj': 46, 'qyvrm': 73}

    def func2(self, a):
        return a()

    def func1(self, a, b):
        return a(b)


a = MyClass()
d = a.func1(a.func2, a.func3)
