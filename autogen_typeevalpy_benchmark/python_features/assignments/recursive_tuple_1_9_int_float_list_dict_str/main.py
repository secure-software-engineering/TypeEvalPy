# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 26


def func2():
    return 88.22


def func3():
    return [11, 5, 69]


def func4():
    return {'istdz': 100, 'hcont': 39, 'eaupg': 93}


def func5():
    return 'kntvg'


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
