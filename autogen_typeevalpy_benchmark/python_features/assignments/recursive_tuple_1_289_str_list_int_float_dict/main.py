# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'tkena'


def func2():
    return [74, 42, 33]


def func3():
    return 11


def func4():
    return 39.87


def func5():
    return {'vljko': 24, 'dqbca': 68, 'sdtgx': 93}


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
