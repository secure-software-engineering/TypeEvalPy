# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 58.76


def func2():
    return 16


def func3():
    return 'dwtxz'


def func4():
    return {'kldnp': 85, 'rzitf': 83, 'ghcow': 95}


def func5():
    return (27, 89, 10)


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
