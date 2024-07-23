# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'lhwrv'


def func2():
    return (63, 11, 47)


def func3():
    return [78, 74, 54]


def func4():
    return 24


def func5():
    return {'pqeto': 21, 'rdruz': 17, 'kmwkh': 82}


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
