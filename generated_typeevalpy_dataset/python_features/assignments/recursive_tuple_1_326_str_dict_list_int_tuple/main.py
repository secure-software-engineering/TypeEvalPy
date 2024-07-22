# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'cvjdo'


def func2():
    return {'dbidh': 87, 'etxvc': 16, 'ufvbw': 50}


def func3():
    return [83, 42, 99]


def func4():
    return 48


def func5():
    return (6, 87, 62)


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
