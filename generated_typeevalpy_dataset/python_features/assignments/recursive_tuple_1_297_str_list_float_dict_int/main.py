# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'sluyd'


def func2():
    return [29, 40, 44]


def func3():
    return 5.72


def func4():
    return {'iivtv': 22, 'gvwlm': 15, 'ylfox': 70}


def func5():
    return 86


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
