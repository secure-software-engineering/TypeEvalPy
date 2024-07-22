# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'limbb': 34, 'zomcr': 62, 'specl': 65}


def func2():
    return 'fpkam'


def func3():
    return [89, 54, 27]


def func4():
    return 61.75


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
