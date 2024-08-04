# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 60


def func2():
    return (83, 69, 60)


def func3():
    return 'cecyk'


def func4():
    return [56, 26, 52]


def func5():
    return {'iizms': 47, 'mhaem': 56, 'qiapj': 61}


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
