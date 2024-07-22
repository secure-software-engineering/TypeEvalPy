# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28


def func2():
    return 67.75


def func3():
    return {'nmrnw': 79, 'nnxjk': 77, 'mcdlc': 71}


def func4():
    return [3, 43, 86]


def func5():
    return (15, 31, 23)


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
