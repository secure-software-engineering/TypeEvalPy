# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'pvvlp'

    def func2(self):
        return {'ytiem': 89, 'ksmrd': 16, 'lvxae': 25}

    def func3(self):
        return False


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
