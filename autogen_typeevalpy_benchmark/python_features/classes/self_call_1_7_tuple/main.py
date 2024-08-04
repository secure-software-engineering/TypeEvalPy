# A function is called inside a class using self.


class MyClass:
    def __init__(self):
        self.func1()

    def func1(self):
        return (76, 23, 68)

    def func2(self):
        return self.func1()


a = MyClass()
b = a.func2()
