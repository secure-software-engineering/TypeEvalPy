# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (90, 29, 35)


def func2():
    return [79, 76, 70]


def func3():
    return 6


def func4():
    return {'bzszo': 16, 'xmqam': 36, 'lbdhv': 38}


def func5():
    return 3.66


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
