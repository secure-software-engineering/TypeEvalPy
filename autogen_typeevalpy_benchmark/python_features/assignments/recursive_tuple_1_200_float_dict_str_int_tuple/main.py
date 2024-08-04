# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 91.06


def func2():
    return {'rhkak': 92, 'dgpzi': 78, 'faibh': 59}


def func3():
    return 'pqiky'


def func4():
    return 2


def func5():
    return (44, 44, 41)


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
