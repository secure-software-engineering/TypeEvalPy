# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jivpq': 3, 'wffts': 40, 'vfhhw': 65}


def func2():
    return 84.22


def func3():
    return 64


def func4():
    return [66, 77, 75]


def func5():
    return 'xamua'


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
