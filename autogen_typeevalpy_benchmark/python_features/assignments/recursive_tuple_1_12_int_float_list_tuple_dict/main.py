# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 12


def func2():
    return 30.31


def func3():
    return [53, 95, 67]


def func4():
    return (48, 61, 82)


def func5():
    return {'onrpz': 26, 'skcbt': 59, 'layvv': 61}


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
