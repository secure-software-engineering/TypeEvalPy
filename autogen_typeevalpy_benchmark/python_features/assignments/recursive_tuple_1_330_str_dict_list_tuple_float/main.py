# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'mlvqn'


def func2():
    return {'isgkc': 82, 'ndzvz': 16, 'knwvc': 87}


def func3():
    return [13, 27, 51]


def func4():
    return (92, 80, 51)


def func5():
    return 63.74


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
