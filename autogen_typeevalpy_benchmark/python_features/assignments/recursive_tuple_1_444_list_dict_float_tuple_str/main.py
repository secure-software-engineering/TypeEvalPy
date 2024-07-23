# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [100, 76, 86]


def func2():
    return {'ggtcz': 37, 'avmnt': 52, 'wuqev': 17}


def func3():
    return 87.35


def func4():
    return (96, 72, 49)


def func5():
    return 'cgsqi'


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
