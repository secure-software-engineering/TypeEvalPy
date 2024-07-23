# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [2, 64, 29]


def func2():
    return 60


def func3():
    return {'kmxdz': 46, 'dkygm': 24, 'dvnnl': 14}


def func4():
    return (63, 35, 97)


def func5():
    return 49.53


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
