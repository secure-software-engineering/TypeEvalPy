# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kgrlw': 10, 'rudmv': 2, 'nbqib': 31}


def func2():
    return (47, 13, 41)


def func3():
    return 'fowvl'


def func4():
    return 59.33


def func5():
    return [75, 34, 46]


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
