# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 93.42


def func2():
    return (83, 100, 12)


def func3():
    return 'pmupu'


def func4():
    return 58


def func5():
    return {'bfceg': 25, 'icxco': 76, 'rqnfv': 25}


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
