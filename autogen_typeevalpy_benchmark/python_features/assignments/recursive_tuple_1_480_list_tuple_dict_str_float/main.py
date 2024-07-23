# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [14, 15, 29]


def func2():
    return (85, 33, 42)


def func3():
    return {'uihnc': 63, 'anixw': 77, 'abbul': 74}


def func4():
    return 'fshol'


def func5():
    return 36.58


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
