# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mlqey': 66, 'detbi': 8, 'ifjbp': 81}


def func2():
    return 'fxypd'


def func3():
    return (51, 11, 8)


def func4():
    return 14.46


def func5():
    return 26


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
