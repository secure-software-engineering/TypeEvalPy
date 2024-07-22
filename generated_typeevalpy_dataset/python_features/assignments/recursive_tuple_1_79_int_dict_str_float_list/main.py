# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 99


def func2():
    return {'jtvtb': 84, 'kcbco': 75, 'dbmov': 22}


def func3():
    return 'shuyy'


def func4():
    return 10.31


def func5():
    return [59, 84, 90]


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
