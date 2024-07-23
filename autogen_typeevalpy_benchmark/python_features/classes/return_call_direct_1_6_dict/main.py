# A method returns a different method and that method is directly called.


class MyClass:
    def func2(self):
        return {'gxjel': 82, 'wxwbc': 91, 'wavxl': 11}

    def func1(self):
        return self.func2


a = MyClass()
b = a.func1()()
