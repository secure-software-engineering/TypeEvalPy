# A function is called inside a class using self.


class MyClass:
    def __init__(self):
        self.func1()

    def func1(self):
        return {'trmxq': 93, 'wugru': 32, 'itbjs': 88}

    def func2(self):
        return self.func1()


a = MyClass()
b = a.func2()
