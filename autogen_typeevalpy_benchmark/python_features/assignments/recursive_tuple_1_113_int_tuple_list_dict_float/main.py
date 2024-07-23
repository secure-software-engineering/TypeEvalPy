# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 61


def func2():
    return (84, 59, 16)


def func3():
    return [43, 77, 64]


def func4():
    return {'epgfg': 44, 'iwlax': 49, 'nsifl': 63}


def func5():
    return 37.83


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
