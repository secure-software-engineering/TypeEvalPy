# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 26


def func2():
    return (12, 45, 91)


def func3():
    return {'ohtmn': 27, 'kferx': 93, 'hkpti': 63}


def func4():
    return 'llphi'


def func5():
    return [14, 78, 50]


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
