# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'fbadk'


def func2():
    return {'fuwlo': 87, 'zfzea': 64, 'sufxe': 15}


def func3():
    return 11


def func4():
    return (86, 59, 44)


def func5():
    return [79, 94, 48]


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
