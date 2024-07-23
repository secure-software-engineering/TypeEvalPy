# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 68


def func2():
    return (32, 75, 77)


def func3():
    return 'lbwhc'


def func4():
    return {'mebuj': 82, 'rkgdu': 86, 'lhutx': 74}


def func5():
    return [87, 58, 26]


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
