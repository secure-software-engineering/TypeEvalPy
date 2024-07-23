# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 38.96


def func2():
    return 'wxspk'


def func3():
    return [32, 58, 87]


def func4():
    return 56


def func5():
    return {'nqpmt': 58, 'ahujs': 19, 'tcypj': 22}


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
