# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (97, 78, 10)


def func2():
    return 78.86


def func3():
    return 81


def func4():
    return 'axouj'


def func5():
    return {'mgrwp': 11, 'cjfgp': 94, 'bunio': 95}


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
