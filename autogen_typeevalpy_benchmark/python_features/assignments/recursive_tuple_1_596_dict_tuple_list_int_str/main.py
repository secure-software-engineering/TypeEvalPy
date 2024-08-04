# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'hyskh': 97, 'vdtlm': 5, 'rkjyx': 55}


def func2():
    return (89, 27, 33)


def func3():
    return [78, 38, 24]


def func4():
    return 80


def func5():
    return 'zvwvm'


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
