# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (74, 40, 90)


def func2():
    return {'tohot': 9, 'vplqr': 94, 'jdpoa': 7}


def func3():
    return 39.46


def func4():
    return [54, 59, 31]


def func5():
    return 'gtjxc'


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
