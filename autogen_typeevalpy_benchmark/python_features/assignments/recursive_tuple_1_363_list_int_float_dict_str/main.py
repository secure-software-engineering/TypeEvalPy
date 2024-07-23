# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [91, 61, 6]


def func2():
    return 57


def func3():
    return 23.25


def func4():
    return {'gjsoj': 84, 'isdof': 87, 'bgpll': 46}


def func5():
    return 'mvruv'


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
