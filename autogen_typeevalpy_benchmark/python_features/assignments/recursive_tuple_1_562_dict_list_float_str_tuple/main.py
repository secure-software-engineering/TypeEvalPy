# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'skjsk': 35, 'ddzyq': 80, 'lzwlw': 38}


def func2():
    return [61, 60, 11]


def func3():
    return 66.58


def func4():
    return 'pqjaz'


def func5():
    return (14, 66, 39)


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
