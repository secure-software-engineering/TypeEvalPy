# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [80, 56, 90]


def func2():
    return {'ejpfg': 87, 'iycyk': 85, 'pwwum': 30}


def func3():
    return 'phlsr'


def func4():
    return (31, 95, 98)


def func5():
    return 36


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
