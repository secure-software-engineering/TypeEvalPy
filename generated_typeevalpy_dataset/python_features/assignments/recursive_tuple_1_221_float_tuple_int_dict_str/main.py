# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 92.52


def func2():
    return (92, 77, 24)


def func3():
    return 49


def func4():
    return {'edbpv': 43, 'ewtqh': 72, 'wteuz': 52}


def func5():
    return 'rehav'


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
