# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'eamti'


def func2():
    return (89, 43, 67)


def func3():
    return 53.55


def func4():
    return 2


def func5():
    return {'ifzoj': 44, 'pfdnw': 45, 'frcei': 10}


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
