# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [62, 21, 1]


def func2():
    return (7, 23, 71)


def func3():
    return 22.16


def func4():
    return {'hdyzd': 9, 'ybchz': 54, 'rtywt': 47}


def func5():
    return 'pssrt'


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
