# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (32, 29, 29)


def func2():
    return [48, 60, 36]


def func3():
    return 55.97


def func4():
    return {'nsmzg': 58, 'cvacb': 86, 'txqth': 25}


def func5():
    return 'alasv'


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
