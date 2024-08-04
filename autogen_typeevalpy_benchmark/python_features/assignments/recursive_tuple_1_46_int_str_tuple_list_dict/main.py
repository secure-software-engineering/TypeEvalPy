# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 5


def func2():
    return 'xnlbq'


def func3():
    return (67, 83, 85)


def func4():
    return [92, 85, 14]


def func5():
    return {'kibau': 29, 'tyjgc': 13, 'kzier': 86}


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
