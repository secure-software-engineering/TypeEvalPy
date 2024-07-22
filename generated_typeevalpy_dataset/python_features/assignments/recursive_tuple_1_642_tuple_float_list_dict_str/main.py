# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (18, 43, 25)


def func2():
    return 68.6


def func3():
    return [33, 36, 14]


def func4():
    return {'aidvq': 49, 'eiffh': 75, 'hsppg': 11}


def func5():
    return 'inpqa'


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
