# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'conzj': 62, 'etsbm': 64, 'styay': 50}


def func2():
    return 10.4


def func3():
    return [6, 55, 97]


def func4():
    return 81


def func5():
    return 'sveqy'


def func6():
    pass


a, (b, c) = func1, (func2, func3)
i = a()
j = b()
k = c()

a, (b, (c, d)) = func1, (func2, (func3, func4))

h = d()

f, b = c, e = func5, func6

l = e()
m = f()
