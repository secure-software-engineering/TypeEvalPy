# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 52.95


def func2():
    return 'gszep'


def func3():
    return [18, 24, 100]


def func4():
    return {'toyyk': 4, 'ceuji': 40, 'zknfr': 73}


def func5():
    return (18, 53, 38)


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
