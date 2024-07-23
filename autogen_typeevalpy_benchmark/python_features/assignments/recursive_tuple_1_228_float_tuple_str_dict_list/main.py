# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 18.2


def func2():
    return (82, 58, 22)


def func3():
    return 'zfkia'


def func4():
    return {'bseqj': 65, 'ocaxq': 25, 'uvxhe': 12}


def func5():
    return [64, 100, 1]


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
