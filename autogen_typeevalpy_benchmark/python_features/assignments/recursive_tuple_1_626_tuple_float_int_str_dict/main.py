# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (57, 22, 78)


def func2():
    return 83.97


def func3():
    return 63


def func4():
    return 'zujjc'


def func5():
    return {'lhodv': 27, 'aspkv': 64, 'nstzj': 57}


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
