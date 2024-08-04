# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [54, 61, 41]


def func2():
    return 'mcvvj'


def func3():
    return {'cpcqc': 51, 'exrpu': 75, 'plxds': 86}


def func4():
    return 62


def func5():
    return 66.79


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
