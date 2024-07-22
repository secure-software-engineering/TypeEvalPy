# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'pfqnm': 78, 'brtii': 11, 'bymcl': 30}


def func2():
    return [57, 4, 44]


def func3():
    return 34


def func4():
    return (10, 41, 21)


def func5():
    return 'fldyl'


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
