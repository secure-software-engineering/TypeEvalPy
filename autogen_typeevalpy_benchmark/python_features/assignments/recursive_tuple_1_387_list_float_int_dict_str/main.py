# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [31, 2, 45]


def func2():
    return 3.14


def func3():
    return 93


def func4():
    return {'mxacv': 55, 'qgtpn': 86, 'ckjhz': 68}


def func5():
    return 'bdqtr'


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
