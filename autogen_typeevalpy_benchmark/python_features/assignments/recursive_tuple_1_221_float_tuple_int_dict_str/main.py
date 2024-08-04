# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 34.64


def func2():
    return (68, 100, 89)


def func3():
    return 95


def func4():
    return {'vlaoa': 99, 'vaflg': 74, 'frilr': 46}


def func5():
    return 'xsoed'


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
