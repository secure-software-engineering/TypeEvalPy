# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (46, 6, 64)


def func2():
    return [65, 82, 53]


def func3():
    return 80


def func4():
    return 'sells'


def func5():
    return {'nfmah': 6, 'bngtg': 2, 'fqtzs': 39}


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
