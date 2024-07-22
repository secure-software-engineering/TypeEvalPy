# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 8


def func2():
    return (15, 94, 43)


def func3():
    return [58, 47, 6]


def func4():
    return {'lpbhh': 5, 'bvnpn': 61, 'rknqr': 77}


def func5():
    return 'zslng'


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
