# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'zyuet'


def func2():
    return {'vrgxy': 87, 'yymld': 56, 'injdv': 54}


def func3():
    return 18


def func4():
    return [64, 32, 45]


def func5():
    return 60.36


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
