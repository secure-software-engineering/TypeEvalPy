# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 28


def func2():
    return [48, 80, 70]


def func3():
    return {'fbijg': 2, 'djpcn': 49, 'mchgz': 87}


def func4():
    return (85, 31, 25)


def func5():
    return 'vgnps'


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
