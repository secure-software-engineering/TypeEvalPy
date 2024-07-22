# We perform tuple assignment on class methods.


class MyClass:
    def __init__(self):
        pass

    def func1(self):
        return 'bibua'

    def func2(self):
        return (81, 29, 87)

    def func3(self):
        return {'cuqgi': 17, 'jpadr': 53, 'hlxpi': 65}


class MyClass2:
    def __init__(self):
        pass


a, b = MyClass(), MyClass2()

c, (d, e) = a.func1, (a.func2, a.func3)

f = c()
g = d()
h = e()
