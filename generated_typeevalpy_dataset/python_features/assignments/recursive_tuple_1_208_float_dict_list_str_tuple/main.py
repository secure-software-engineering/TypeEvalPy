# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 41.04


def func2():
    return {'uthxu': 58, 'clook': 28, 'cdjog': 64}


def func3():
    return [89, 37, 72]


def func4():
    return 'hbinu'


def func5():
    return (6, 72, 22)


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
