# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 14.7


def func2():
    return 'rcfxz'


def func3():
    return 100


def func4():
    return {'tfgol': 87, 'kdpll': 24, 'vadps': 94}


def func5():
    return [86, 13, 1]


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
