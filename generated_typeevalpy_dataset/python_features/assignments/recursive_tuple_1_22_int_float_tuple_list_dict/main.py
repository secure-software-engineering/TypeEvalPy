# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 26


def func2():
    return 58.75


def func3():
    return (56, 48, 93)


def func4():
    return [98, 70, 25]


def func5():
    return {'mnpnm': 39, 'bfghw': 21, 'rzuga': 84}


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
