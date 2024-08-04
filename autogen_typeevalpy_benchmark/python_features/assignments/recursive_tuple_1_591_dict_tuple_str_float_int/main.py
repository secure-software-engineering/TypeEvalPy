# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mohlb': 91, 'nqujn': 62, 'eteus': 18}


def func2():
    return (52, 23, 3)


def func3():
    return 'tgmru'


def func4():
    return 36.88


def func5():
    return 28


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
