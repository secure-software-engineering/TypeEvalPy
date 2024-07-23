# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'tkimm': 6, 'cgtkh': 83, 'erbez': 6}


def func2():
    return 63.06


def func3():
    return 'geczp'


def func4():
    return 35


def func5():
    return (31, 36, 11)


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
