# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 24


def func2():
    return {'bbtfm': 43, 'xceyj': 47, 'hcaow': 95}


def func3():
    return 'vtppg'


def func4():
    return (36, 27, 75)


def func5():
    return [50, 12, 14]


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
