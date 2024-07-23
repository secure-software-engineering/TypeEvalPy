# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pdayq'


def func2():
    return 57


def func3():
    return (78, 3, 18)


def func4():
    return {'lbexe': 6, 'drudv': 44, 'lnvob': 26}


def func5():
    return [1, 52, 5]


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
