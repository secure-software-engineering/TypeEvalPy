# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (16, 93, 2)


def func2():
    return 61


def func3():
    return 91.13


def func4():
    return 'xhmah'


def func5():
    return {'yjjgv': 27, 'vczyy': 43, 'hjprp': 4}


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
