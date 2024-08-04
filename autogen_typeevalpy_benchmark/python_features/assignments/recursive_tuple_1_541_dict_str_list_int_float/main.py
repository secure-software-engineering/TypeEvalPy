# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qrlnp': 78, 'puyoo': 81, 'bmgtx': 89}


def func2():
    return 'xoenw'


def func3():
    return [79, 66, 59]


def func4():
    return 98


def func5():
    return 27.69


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
