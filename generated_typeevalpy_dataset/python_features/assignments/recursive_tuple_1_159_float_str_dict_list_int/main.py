# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 89.35


def func2():
    return 'lnzya'


def func3():
    return {'pukfv': 60, 'owlui': 17, 'djibt': 64}


def func4():
    return [36, 88, 61]


def func5():
    return 72


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
