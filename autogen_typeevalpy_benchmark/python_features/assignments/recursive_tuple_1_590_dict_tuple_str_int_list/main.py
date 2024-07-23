# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'vppre': 45, 'klgqo': 71, 'zrrzv': 35}


def func2():
    return (98, 33, 55)


def func3():
    return 'mnyhd'


def func4():
    return 25


def func5():
    return [8, 83, 65]


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
