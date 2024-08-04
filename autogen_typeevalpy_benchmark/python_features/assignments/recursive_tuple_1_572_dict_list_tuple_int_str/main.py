# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'pvvif': 32, 'djbmj': 30, 'uokhs': 86}


def func2():
    return [79, 43, 30]


def func3():
    return (40, 71, 12)


def func4():
    return 12


def func5():
    return 'aadtx'


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
